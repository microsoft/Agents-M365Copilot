from enum import Enum

class EdgeTelemetryMode(str, Enum):
    # Default – No telemetry data collected or sent
    NotConfigured = "notConfigured",
    # Allow sending intranet history only: Only send browsing history data for intranet sites
    Intranet = "intranet",
    # Allow sending internet history only: Only send browsing history data for internet sites
    Internet = "internet",
    # Allow sending both intranet and internet history: Send browsing history data for intranet and internet sites
    IntranetAndInternet = "intranetAndInternet",

