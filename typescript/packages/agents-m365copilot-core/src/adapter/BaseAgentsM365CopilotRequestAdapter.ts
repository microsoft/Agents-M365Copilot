import {
  AuthenticationProvider,
  ParseNodeFactory,
  ParseNodeFactoryRegistry,
  SerializationWriterFactory,
  SerializationWriterFactoryRegistry,
} from "@microsoft/kiota-abstractions";
import { HttpClient, type ObservabilityOptions, ObservabilityOptionsImpl } from "@microsoft/kiota-http-fetchlibrary";
import { DefaultRequestAdapter } from "@microsoft/kiota-bundle";
import { createAgentsM365CopilotClient } from "../http/agentsM365CopilotClientFactory.js";

/**
 * Base request adapter for AgentsM365Copilot clients. Bootstraps telemetry and other aspects.
 */
export class BaseAgentsM365CopilotRequestAdapter extends DefaultRequestAdapter {
  /**
   * Instantiates a new request adapter.
   * @param graphServiceTargetVersion the target version of the api endpoint we are targeting ("" or beta).
   * @param graphServiceLibraryClientVersion the version of the service library in use. Should be in the format `x.x.x` (Semantic version).
   * @param authenticationProvider the authentication provider to use.
   * @param parseNodeFactory the parse node factory to deserialize responses.
   * @param serializationWriterFactory the serialization writer factory to use to serialize request bodies.
   * @param httpClient the http client to use to execute requests.
   * @param observabilityOptions the observability options to use.
   */
  public constructor(
    agentsM365CopilotServiceTargetVersion: string,
    agentsM365CopilotServiceLibraryClientVersion: string,
    authenticationProvider: AuthenticationProvider,
    parseNodeFactory: ParseNodeFactory = new ParseNodeFactoryRegistry(),
    serializationWriterFactory: SerializationWriterFactory = new SerializationWriterFactoryRegistry(),
    httpClient: HttpClient = createAgentsM365CopilotClient({
      agentsM365CopilotServiceTargetVersion,
      agentsM365CopilotServiceLibraryClientVersion,
    }),
    observabilityOptions: ObservabilityOptions = new ObservabilityOptionsImpl(),
  ) {
    super(authenticationProvider, parseNodeFactory, serializationWriterFactory, httpClient, observabilityOptions);
  }
}
