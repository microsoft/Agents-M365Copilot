export interface AgentsM365CopilotTelemetryOption {
  /**
   * The target version of the api endpoint we are targeting (v1 or beta)
   */
  graphServiceTargetVersion?: string;
  /**
   * The version of the service library in use. Should be in the format `x.x.x` (Semantic version)
   */
  graphServiceLibraryClientVersion?: string;
  /**
   * The product prefix to use in setting the telemetry headers.
   * Will default to `graph-javascript` if not set.
   */
  graphProductPrefix?: string;
}
