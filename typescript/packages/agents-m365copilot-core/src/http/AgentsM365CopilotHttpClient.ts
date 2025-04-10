import { HttpClient, type Middleware } from "@microsoft/kiota-http-fetchlibrary";
import { AgentsM365CopilotTelemetryOption, getDefaultMiddlewares } from "../middleware/index.js";

/**
 * Specialized version of the HTTP client for the Agents M365 Copilot API that bootstraps telemetry, /me replacement, and other aspects
 */
export class AgentsM365CopilotHttpClient extends HttpClient {
  /**
   * Creates a new instance of the GraphHttpClient class
   * @param agentsM365CopilotTelemetryOption The options for telemetry
   * @param customFetch The custom fetch implementation to use
   * @param middlewares The middlewares to use
   */
  public constructor(
    agentsM365CopilotTelemetryOption: AgentsM365CopilotTelemetryOption,
    customFetch?: (request: string, init: RequestInit) => Promise<Response>,
    ...middlewares: Middleware[]
  ) {
    super(
      customFetch,
      ...((middlewares ?? []).length > 0
        ? middlewares
        : getDefaultMiddlewares({
            customFetch,
            agentsM365CopilotTelemetryOption,
          })),
    );
  }
}
