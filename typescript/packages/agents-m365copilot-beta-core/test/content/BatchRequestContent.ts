import { assert, describe, it } from "vitest";
import { BatchRequestContent, BatchResponseContent } from "../../src";
// @ts-ignore
import { DummyRequestAdapter } from "../utils/DummyRequestAdapter";
import {
  RequestInformation,
  HttpMethod,
  ErrorMappings,
  ParseNode,
  Parsable,
  Headers,
  ParseNodeFactoryRegistry,
} from "@microsoft/kiota-abstractions";
import { JsonParseNodeFactory } from "@microsoft/kiota-serialization-json";
// @ts-ignore
import { createGraphErrorFromDiscriminatorValue } from "../tasks/PageIterator";
import { createCipheriv } from "node:crypto";

const adapter = new DummyRequestAdapter();

const errorMappings: ErrorMappings = {
  XXX: parseNode => createGraphErrorFromDiscriminatorValue(parseNode),
};

interface SampleResponse {
  value: number[];
  additionalContent?: string;
  id?: string;
  name?: string;
}

export const createSampleFromDiscriminatorValue = (
  _parseNode: ParseNode | undefined,
): ((instance?: Parsable) => Record<string, (node: ParseNode) => void>) => {
  return deserializeIntoSample;
};

export const deserializeIntoSample = (
  sampleResponse: Partial<SampleResponse> | undefined = {},
): Record<string, (node: ParseNode) => void> => {
  return {
    value: n => {
      sampleResponse.value = n.getCollectionOfPrimitiveValues<number>();
    },
    additionalContent: n => {
      sampleResponse.additionalContent = n.getStringValue();
    },
    id: n => {
      sampleResponse.id = n.getStringValue();
    },
    name: n => {
      sampleResponse.name = n.getStringValue();
    },
  };
};

describe("BatchRequestContent tests", () => {
  describe("Constructor", () => {
    it("Should create instance", () => {
      const requestContent = new BatchRequestContent(adapter, errorMappings);
      assert(requestContent instanceof BatchRequestContent);
    });
  });
  describe("AddRequest", () => {
    it("Should add request", () => {
      const requestContent = new BatchRequestContent(adapter, errorMappings);

      const requestInfo = new RequestInformation(HttpMethod.GET, "{+baseurl}/me");
      requestInfo.headers = new Headers();
      requestInfo.headers.add("Content-Type", "application/json");
      const batchItem = requestContent.addBatchRequest(requestInfo);

      assert.isNotNull(batchItem);
      assert.isDefined(batchItem.id);
      assert.isTrue(batchItem.id.length > 0);
      assert.equal(requestContent.requests.size, 1);
      assert.equal(batchItem.method, requestInfo.httpMethod?.toString());
      assert.equal(batchItem.url, requestInfo.URL);
    });
    it("Should respect maximum number of steps", () => {
      const requestContent = new BatchRequestContent(adapter, errorMappings);

      // create a loop of 20
      for (let i = 0; i < 20; i++) {
        const requestInfo = new RequestInformation(HttpMethod.GET, "{+baseurl}/me");
        requestContent.addBatchRequest(requestInfo);
      }

      assert.throws(
        () => {
          const requestInfo = new RequestInformation(HttpMethod.GET, "{+baseurl}/me");
          requestContent.addBatchRequest(requestInfo);
        },
        Error,
        "Maximum requests limit exceeded, Max allowed number of requests are 20",
      );
    });
    it("Get content validates depends on", () => {
      const requestContent = new BatchRequestContent(adapter, errorMappings);

      const requestInfo = new RequestInformation(HttpMethod.GET, "{+baseurl}/me");
      const batchItem = requestContent.addBatchRequest(requestInfo);

      const requestInfo2 = new RequestInformation(HttpMethod.GET, "{+baseurl}/me/messages");
      const batchItem2 = requestContent.addBatchRequest(requestInfo2);

      batchItem2.dependsOn = [batchItem.id];

      assert.doesNotThrow(() => requestContent.getContent());

      batchItem2.dependsOn = ["random"];
      assert.throws(
        () => {
          requestContent.getContent();
        },
        Error,
        "Invalid dependency chain found in the requests, Please provide valid dependency chain",
      );
    });
  });

  describe("PostRequest", () => {
    it("Should post a serialized batch of objects to the adapter", () => {
      const requestContent = new BatchRequestContent(adapter, errorMappings);

      const requestInfo = new RequestInformation(HttpMethod.GET, "{+baseurl}/me");
      const request = requestContent.addBatchRequest(requestInfo);

      const requestInfo2 = new RequestInformation(HttpMethod.GET, "{+baseurl}/me/messages");
      requestContent.addBatchRequest(requestInfo2);

      adapter.setResponse({ responses: { id: request.id, status: 200 } });

      const result = requestContent.postAsync();
      assert.isNotNull(result);

      const response = adapter.getRequests()[0];
      assert.equal(response.httpMethod, HttpMethod.POST);
      assert.equal(response.URL, "/$batch");
    });
  });

  describe("ResponseContent", () => {
    it("Can fetch a response by Id", () => {
      const requestContent = new BatchResponseContent({
        responses: [
          { id: "1", status: 200, headers: {} },
          { id: "2", status: 204, headers: {} },
        ],
      });

      const response = requestContent.getResponseById("1");
      assert.isNotNull(response);
      assert.equal(response?.status, 200);
    });
    it("Can parse a response a response by Id", () => {
      if (!(adapter.getParseNodeFactory() instanceof ParseNodeFactoryRegistry)) {
        throw new Error("Invalid parse node factory");
      }
      const parseNodeFactoryRegistry = adapter.getParseNodeFactory() as ParseNodeFactoryRegistry;
      parseNodeFactoryRegistry.registerDefaultDeserializer(JsonParseNodeFactory, adapter.getBackingStoreFactory());

      const sampleArrayBuffer = new TextEncoder().encode(JSON.stringify({ value: [1, 2, 3], id: "1", name: "test" }));
      const requestContent = new BatchResponseContent({
        responses: [{ id: "1", status: 200, headers: {}, body: sampleArrayBuffer }],
      });

      const response = requestContent.getParsableResponseById<SampleResponse>(
        "1",
        parseNodeFactoryRegistry as ParseNodeFactoryRegistry,
        createSampleFromDiscriminatorValue,
      );
      assert.isNotNull(response);
      assert.equal(response?.value.length, 3);
      assert.equal(response?.id, "1");
      assert.equal(response?.name, "test");
    });
  });
});
