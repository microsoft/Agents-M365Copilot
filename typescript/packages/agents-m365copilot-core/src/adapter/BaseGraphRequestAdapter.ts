import {
  AuthenticationProvider,
  ParseNodeFactory,
  ParseNodeFactoryRegistry,
  SerializationWriterFactory,
  SerializationWriterFactoryRegistry,
} from "@microsoft/kiota-abstractions";
import { HttpClient, type ObservabilityOptions, ObservabilityOptionsImpl } from "@microsoft/kiota-http-fetchlibrary";
import { DefaultRequestAdapter } from "@microsoft/kiota-bundle";
import { createAgentsM365CopilotClientFactory } from "../http/GraphClientFactory.js";

/**
 * Base request adapter for graph clients. Bootstraps telemetry and other aspects.
 */
export class BaseGraphRequestAdapter extends DefaultRequestAdapter {
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
    graphServiceTargetVersion: string,
    graphServiceLibraryClientVersion: string,
    authenticationProvider: AuthenticationProvider,
    parseNodeFactory: ParseNodeFactory = new ParseNodeFactoryRegistry(),
    serializationWriterFactory: SerializationWriterFactory = new SerializationWriterFactoryRegistry(),
    httpClient: HttpClient = createAgentsM365CopilotClientFactory({
      graphServiceTargetVersion,
      graphServiceLibraryClientVersion,
    }),
    observabilityOptions: ObservabilityOptions = new ObservabilityOptionsImpl(),
  ) {
    super(authenticationProvider, parseNodeFactory, serializationWriterFactory, httpClient, observabilityOptions);
  }
}
