from enum import Enum

class AlertType(str, Enum):
    UnhealthyRemoteNetworks = "unhealthyRemoteNetworks",
    UnhealthyConnectors = "unhealthyConnectors",
    DeviceTokenInconsistency = "deviceTokenInconsistency",
    CrossTenantAnomaly = "crossTenantAnomaly",
    SuspiciousProcess = "suspiciousProcess",
    ThreatIntelligenceTransactions = "threatIntelligenceTransactions",
    UnknownFutureValue = "unknownFutureValue",
    WebContentBlocked = "webContentBlocked",
    Malware = "malware",
    PatientZero = "patientZero",
    Dlp = "dlp",

