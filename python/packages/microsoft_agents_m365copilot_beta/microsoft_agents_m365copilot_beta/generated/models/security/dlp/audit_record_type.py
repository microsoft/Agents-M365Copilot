from enum import Enum

class AuditRecordType(str, Enum):
    Unknown = "unknown",
    SharePointFileOperation = "sharePointFileOperation",
    ComplianceDlpSharePoint = "complianceDlpSharePoint",
    ComplianceDlpExchange = "complianceDlpExchange",
    DlpEndpoint = "dlpEndpoint",
    ComplianceDlpEndpoint = "complianceDlpEndpoint",
    PowerBiDlp = "powerBiDlp",
    ComplianceDlpApplications = "complianceDlpApplications",
    UnknownFutureValue = "unknownFutureValue",

