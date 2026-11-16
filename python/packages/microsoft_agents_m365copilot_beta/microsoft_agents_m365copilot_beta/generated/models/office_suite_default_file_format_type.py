from enum import Enum

class OfficeSuiteDefaultFileFormatType(str, Enum):
    # No file format selected
    NotConfigured = "notConfigured",
    # Office Open XML Format selected
    OfficeOpenXMLFormat = "officeOpenXMLFormat",
    # Office Open Document Format selected
    OfficeOpenDocumentFormat = "officeOpenDocumentFormat",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

