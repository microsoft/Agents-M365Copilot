import { FetchRequestInit, TelemetryHandler, appendRequestHeader } from "@microsoft/kiota-http-fetchlibrary";
import { AgentsM365CopilotTelemetryOption } from "./agentsM365CopilotTelemetryOption";
import { type RequestOption } from "@microsoft/kiota-abstractions";
import { coreVersion } from "../utils/Version.js";

/**
 * Adds telemetry headers to requests made to the Agents M365 Copilot API
 */
export class AgentsM365CopilotTelemetryHandler extends TelemetryHandler {
  /**
   * Creates a new instance of the AgentsM365CopilotTelemetryHandler class
   */
  public constructor(agentsM365CopilotTelemetryOption: AgentsM365CopilotTelemetryOption) {
    const productPrefix =
      agentsM365CopilotTelemetryOption.agentsM365CopilotProductPrefix ?? "agents-M365-copilot-typescript";
    const coreProduct = `${productPrefix}-core/${coreVersion}`;
    let product = "";
    if (agentsM365CopilotTelemetryOption.agentsM365CopilotServiceLibraryClientVersion) {
      const serviceLibVersion = agentsM365CopilotTelemetryOption.agentsM365CopilotServiceTargetVersion
        ? `-${agentsM365CopilotTelemetryOption.agentsM365CopilotServiceTargetVersion}`
        : "";
      product = `${productPrefix}${serviceLibVersion}/${agentsM365CopilotTelemetryOption.agentsM365CopilotServiceLibraryClientVersion}`;
    }
    const versionHeaderValue = product ? `${product}, ${coreProduct}` : coreProduct;
    super({
      telemetryConfigurator: (
        _url: string,
        requestInit: RequestInit,
        _requestOptions?: Record<string, RequestOption>,
        _telemetryInformation?: unknown,
      ) => {
        appendRequestHeader(requestInit as FetchRequestInit, "SdkVersion", versionHeaderValue);
      },
      getKey: () => "agentsM365CopilotTelemetryOption",
    });
  }
}
