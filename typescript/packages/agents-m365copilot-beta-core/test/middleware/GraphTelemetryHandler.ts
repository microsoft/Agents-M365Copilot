import { assert, describe, it } from "vitest";
import { GraphTelemetryHandler } from "../../src/middleware/GraphTelemetryHandler";
import { GraphTelemetryOption } from "../../src/middleware/GraphTelemetryOption";
import { DummyFetchHandler } from "./DummyFetchHandler";
import { coreVersion } from "../../src/utils/Version";

const options: GraphTelemetryOption = {
  graphServiceTargetVersion: "v1",
  graphProductPrefix: "graph-typescript-test",
  graphServiceLibraryClientVersion: "0.0.0",
};

describe("GraphTelemetryHandler tests", () => {
  it("should initialize", () => {
    const handler = new GraphTelemetryHandler(options);
    assert(handler, "GraphTelemetryHandler failed to initialize");
  });
  it("should add the header", () => {
    const handler = new GraphTelemetryHandler(options);
    const fetchHandler = new DummyFetchHandler();
    fetchHandler.setResponses([new Response()]);
    handler.next = fetchHandler;
    const requestUrl = "https://graph.microsoft.com/v1.0/me";
    const fetchRequestInit = {
				method: "GET",
    };
    handler.execute(requestUrl, fetchRequestInit);
    const headerValue = (fetchRequestInit as any).headers["SdkVersion"];
    assert.equal(headerValue, `graph-typescript-test-v1/0.0.0, graph-typescript-test-core/${coreVersion}`, "SdkVersion header value is incorrect");
  })
});
