import { assert, describe, it } from "vitest";
import { AgentsM365CopilotHttpClient, AgentsM365CopilotTelemetryOption } from "../../src";
import { BaseBearerTokenAuthenticationProvider } from "@microsoft/kiota-abstractions";
import type { Middleware } from "@microsoft/kiota-http-fetchlibrary";
import { createAgentsM365CopilotClientFactory } from "../../src/http/GraphClientFactory";

const graphTelemetryOption: AgentsM365CopilotTelemetryOption = {};

/**
 * Counts the number of middlewares in a linked list of middlewares.
 *
 * @param {Middleware} middleware - The starting middleware.
 * @returns {number} The count of middlewares.
 */
const countMiddlewares = (middleware: Middleware): number => {
  let count = 0;
  while (middleware.next) {
    count++;
    middleware = middleware.next;
  }
  return count;
};

describe("GraphHttpClient tests", () => {
  describe("Constructor", () => {
    it("Should create instance of graph http client", () => {
      const client = new AgentsM365CopilotHttpClient(graphTelemetryOption);
      assert.isNotNull(client, "Client is null");
    });

    it("Should create instance of graph http client with middleware", () => {
      const middleware = {} as Middleware;
      const client = new AgentsM365CopilotHttpClient(graphTelemetryOption, undefined, middleware);
      assert.isNotNull(client, "Client is null");
    });

    it("Should add auth middleware when provider is given", () => {
      const client = new AgentsM365CopilotHttpClient(graphTelemetryOption);
      const count = countMiddlewares((client as any)["middleware"] as Middleware);
      assert.equal(8, count);

      const authenticationProvider = new BaseBearerTokenAuthenticationProvider({} as any);
      const clientWithProvider = createAgentsM365CopilotClientFactory(
        graphTelemetryOption,
        undefined,
        authenticationProvider,
      );
      const count2 = countMiddlewares((clientWithProvider as any)["middleware"] as Middleware);
      assert.equal(9, count2);
    });
  });
});
