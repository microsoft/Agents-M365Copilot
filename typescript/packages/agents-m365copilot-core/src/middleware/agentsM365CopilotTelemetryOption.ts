export interface AgentsM365CopilotTelemetryOption {
  /**
   * The target version of the api endpoint we are targeting (v1 or beta)
   */
  agentsM365CopilotServiceTargetVersion?: string;
  /**
   * The version of the service library in use. Should be in the format `x.x.x` (Semantic version)
   */
  agentsM365CopilotServiceLibraryClientVersion?: string;
  /**
   * The product prefix to use in setting the telemetry headers.
   * Will default to `agentsM365Copilot-javascript` if not set.
   */
  agentsM365CopilotProductPrefix?: string;
}
