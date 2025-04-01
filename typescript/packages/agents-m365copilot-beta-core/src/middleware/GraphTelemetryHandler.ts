import { FetchRequestInit, TelemetryHandler, appendRequestHeader } from "@microsoft/kiota-http-fetchlibrary";
import { GraphTelemetryOption } from "./GraphTelemetryOption.js";
import { type RequestOption } from "@microsoft/kiota-abstractions";
import { coreVersion } from "../utils/Version.js";

/**
 * Adds telemetry headers to requests made to the Graph API
 */
export class GraphTelemetryHandler extends TelemetryHandler {
  /**
   * Creates a new instance of the GraphTelemetryHandler class
   */
  public constructor(graphTelemetryOption: GraphTelemetryOption) {
    const productPrefix = graphTelemetryOption.graphProductPrefix ?? "graph-typescript";
    const coreProduct = `${productPrefix}-core/${coreVersion}`;
    let product = "";
    if (graphTelemetryOption.graphServiceLibraryClientVersion) {
      const serviceLibVersion = graphTelemetryOption.graphServiceTargetVersion
        ? `-${graphTelemetryOption.graphServiceTargetVersion}`
        : "";
      product = `${productPrefix}${serviceLibVersion}/${graphTelemetryOption.graphServiceLibraryClientVersion}`;
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
      getKey: () => "graphTelemetryOption",
    });
  }
}
