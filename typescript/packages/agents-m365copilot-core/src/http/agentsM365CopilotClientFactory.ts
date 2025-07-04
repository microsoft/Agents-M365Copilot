import { BaseBearerTokenAuthenticationProvider } from "@microsoft/kiota-abstractions";
import { Middleware } from "@microsoft/kiota-http-fetchlibrary";
import { AgentsM365CopilotHttpClient } from "./agentsM365CopilotHttpClient";
import { getDefaultMiddlewares, AgentsM365CopilotTelemetryOption } from "../middleware/index.js";

/**
 * Creates an instance of `AgentsM365CopilotHttpClient`, with the provided middlewares and custom fetch implementation both parameters are optional.
 * if no middlewares are provided, the default middlewares will be used.
 * @param {AgentsM365CopilotTelemetryOption} telemetryOption - The telemetry options for the Agents M365 Copilot client.
 * @param {(request: string, init: RequestInit) => Promise<Response>} customFetch - The custom fetch function to use for HTTP requests.
 * @param {BaseBearerTokenAuthenticationProvider} [authenticationProvider] - Optional authentication provider for bearer token.
 * @param {Middleware[]} [middlewares] - Optional array of middleware to use in the HTTP pipeline.
 * @returns {AgentsM365CopilotHttpClient} - A new instance of `AgentsM365CopilotHttpClient`.
 * @example
 * ```Typescript
 * // Example usage of createAgentsM365CopilotClient method with agentsM365CopilotTelemetryOption , customFetch and middlewares parameters provided
 *  createAgentsM365CopilotClient(agentsM365CopilotTelemetryOption, customFetch, [middleware1, middleware2]);
 * ```
 * @example
 * ```Typescript
 * // Example usage of createAgentsM365CopilotClient method with only agentsM365CopilotTelemetryOption and customFetch parameter provided
 * createAgentsM365CopilotClient(agentsM365CopilotTelemetryOption, customFetch);
 * ```
 * @example
 * ```Typescript
 * // Example usage of createAgentsM365CopilotClient method with only agentsM365CopilotTelemetryOption and middlewares parameter provided
 * createAgentsM365CopilotClient(agentsM365CopilotTelemetryOption, undefined, [middleware1, middleware2]);
 * ```
 * @example
 * ```Typescript
 * // Example usage of createAgentsM365CopilotClient method with only agentsM365CopilotTelemetryOption parameter provided
 * createAgentsM365CopilotClient(agentsM365CopilotTelemetryOption);
 * ```
 */
export const createAgentsM365CopilotClient = (
  agentsM365CopilotTelemetryOption: AgentsM365CopilotTelemetryOption,
  customFetch?: (request: string, init: RequestInit) => Promise<Response>,
  authenticationProvider?: BaseBearerTokenAuthenticationProvider,
  middlewares?: Middleware[],
): AgentsM365CopilotHttpClient => {
  const middleware =
    middlewares ||
    getDefaultMiddlewares(
      {
        customFetch,
        agentsM365CopilotTelemetryOption,
      },
      authenticationProvider,
    );
  return new AgentsM365CopilotHttpClient(agentsM365CopilotTelemetryOption, customFetch, ...middleware);
};
