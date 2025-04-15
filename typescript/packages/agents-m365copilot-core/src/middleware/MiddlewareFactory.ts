import {
  Middleware,
  MiddlewareFactory,
  UrlReplaceHandler,
  UrlReplaceHandlerOptions,
  AuthorizationHandler,
} from "@microsoft/kiota-http-fetchlibrary";
import { AgentsM365CopilotTelemetryOption } from "./agentsM365CopilotTelemetryOption";
import { AgentsM365CopilotTelemetryHandler } from "./agentsM365CopilotTelemetryHandler";
import { defaultUrlReplacementPairs } from "../utils/Constants.js";
import { BaseBearerTokenAuthenticationProvider } from "@microsoft/kiota-abstractions";

export const getDefaultMiddlewares = (
  options: MiddlewareFactoryOptions = { customFetch: fetch },
  authenticationProvider?: BaseBearerTokenAuthenticationProvider | null,
): Middleware[] => {
  let kiotaChain = MiddlewareFactory.getDefaultMiddlewares(options?.customFetch);
  if (authenticationProvider) {
    kiotaChain.unshift(new AuthorizationHandler(authenticationProvider));
  }
  const additionalMiddleware: Middleware[] = [
    new UrlReplaceHandler(
      new UrlReplaceHandlerOptions({
        enabled: true,
        urlReplacements: defaultUrlReplacementPairs,
      }),
    ),
  ];
  if (options.agentsM365CopilotTelemetryOption) {
    additionalMiddleware.push(new AgentsM365CopilotTelemetryHandler(options.agentsM365CopilotTelemetryOption));
  }
  const fetchMiddleware = kiotaChain.slice(-1);
  const otherMiddlewares = kiotaChain.slice(0, kiotaChain.length - 1);
  kiotaChain = [...otherMiddlewares, ...additionalMiddleware, ...fetchMiddleware];
  return kiotaChain;
};
interface MiddlewareFactoryOptions {
  customFetch?: (request: string, init: RequestInit) => Promise<Response>;
  agentsM365CopilotTelemetryOption?: AgentsM365CopilotTelemetryOption;
}
