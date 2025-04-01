import { ErrorMappings, HttpMethod, RequestAdapter, RequestInformation } from "@microsoft/kiota-abstractions";
import {
  BatchResponseBody,
  createBatchResponseContentFromDiscriminatorValue,
  serializeBatchRequestBody,
} from "./BatchRequestStep.js";
import { BatchResponseContent } from "./BatchResponseContent.js";
import { BatchRequestContent } from "./BatchRequestContent.js";
import { BatchRequestContentCollection } from "./BatchRequestContentCollection.js";
import { BatchResponseContentCollection } from "./BatchResponseContentCollection.js";

export class BatchRequestBuilder {
  /**
   * @private
   * @static
   * Executes the requests in the batch request content
   */
  private readonly requestAdapter: RequestAdapter;

  /**
   * @private
   * @static
   * Error mappings to be used while deserializing the response
   */
  private readonly errorMappings: ErrorMappings;

  /**
   * Creates an instance of BatchRequestContent.
   * @param {RequestAdapter} requestAdapter - The request adapter to be used for executing the requests.
   * @param {ErrorMappings} errorMappings - The error mappings to be used while deserializing the response.
   * @throws {Error} If the request adapter is undefined.
   * @throws {Error} If the error mappings are undefined.
   */
  constructor(requestAdapter: RequestAdapter, errorMappings: ErrorMappings) {
    if (!requestAdapter) {
      const error = new Error("Request adapter is undefined, Please provide a valid request adapter");
      error.name = "Invalid Request Adapter Error";
      throw error;
    }
    this.requestAdapter = requestAdapter;
    if (!errorMappings) {
      const error = new Error("Error mappings are undefined, Please provide a valid error mappings");
      error.name = "Invalid Error Mappings Error";
      throw error;
    }
    this.errorMappings = errorMappings;
  }

  /**
   * @public
   * @async
   * Executes the batch request
   */
  public async postBatchResponseContentAsync(
    batchRequestContent: BatchRequestContent,
  ): Promise<BatchResponseContent | undefined> {
    const requestInformation = new RequestInformation();
    requestInformation.httpMethod = HttpMethod.POST;
    requestInformation.urlTemplate = "{+baseurl}/$batch";

    const content = batchRequestContent.getContent();
    requestInformation.setContentFromParsable(
      this.requestAdapter,
      "application/json",
      content,
      serializeBatchRequestBody,
    );

    requestInformation.headers.add("Content-Type", "application/json");

    const result = await this.requestAdapter.send<BatchResponseBody>(
      requestInformation,
      createBatchResponseContentFromDiscriminatorValue,
      this.errorMappings,
    );

    if (result === undefined) {
      return undefined;
    } else {
      return new BatchResponseContent(result);
    }
  }

  /**
   * Executes the batch requests asynchronously.
   *
   * @returns {Promise<BatchResponseContent | undefined>} A promise that resolves to the batch response content or undefined.
   * @throws {Error} If the batch limit is exceeded.
   */
  public async postBatchRequestContentCollectionAsync(
    collection: BatchRequestContentCollection,
  ): Promise<BatchResponseContentCollection | undefined> {
    // chuck the batch requests into smaller batches
    const batches = collection.getBatchResponseContents();

    // loop over batches and create batch request body
    const batchResponseBody: BatchResponseContent[] = [];
    for (const requestContent of batches) {
      const response = await requestContent.postAsync();
      if (response) {
        batchResponseBody.push(response);
      }
    }
    return new BatchResponseContentCollection(batchResponseBody);
  }
}
