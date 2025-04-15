import { assert, describe, it } from "vitest";
import { AgentsM365CopilotTelemetryHandler } from "../../src/middleware/agentsM365CopilotTelemetryHandler";
import { AgentsM365CopilotTelemetryOption } from "../../src/middleware/agentsM365CopilotTelemetryOption";
import { DummyFetchHandler } from "./DummyFetchHandler";
import { coreVersion } from "../../src/utils/Version";

const options: AgentsM365CopilotTelemetryOption = {
  agentsM365CopilotServiceTargetVersion: "v1",
  agentsM365CopilotProductPrefix: "agents-M365-copilot-typescript-test",
  agentsM365CopilotServiceLibraryClientVersion: "0.0.0",
};

describe("AgentsM365CopilotTelemetryHandler tests", () => {
  it("should initialize", () => {
    const handler = new AgentsM365CopilotTelemetryHandler(options);
    assert(handler, "AgentsM365CopilotTelemetryHandler failed to initialize");
  });
  it("should add the header", () => {
    const handler = new AgentsM365CopilotTelemetryHandler(options);
    const fetchHandler = new DummyFetchHandler();
    fetchHandler.setResponses([new Response()]);
    handler.next = fetchHandler;
    const requestUrl = "https://graph.microsoft.com/v1.0/me";
    const fetchRequestInit = {
      method: "GET",
    };
    handler.execute(requestUrl, fetchRequestInit);
    const headerValue = (fetchRequestInit as any).headers["SdkVersion"];
    assert.equal(
      headerValue,
      `agents-M365-copilot-typescript-test-v1/0.0.0, agents-M365-copilot-typescript-test-core/${coreVersion}`,
      "SdkVersion header value is incorrect",
    );
  });
});
