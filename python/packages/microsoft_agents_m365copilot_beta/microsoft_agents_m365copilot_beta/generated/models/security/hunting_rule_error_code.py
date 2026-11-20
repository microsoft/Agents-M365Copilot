from enum import Enum

class HuntingRuleErrorCode(str, Enum):
    QueryExecutionFailed = "queryExecutionFailed",
    QueryExecutionThrottling = "queryExecutionThrottling",
    QueryExceededResultSize = "queryExceededResultSize",
    QueryLimitsExceeded = "queryLimitsExceeded",
    QueryTimeout = "queryTimeout",
    AlertCreationFailed = "alertCreationFailed",
    AlertReportNotFound = "alertReportNotFound",
    PartialRowsFailed = "partialRowsFailed",
    UnknownFutureValue = "unknownFutureValue",
    NoImpactedEntity = "noImpactedEntity",

