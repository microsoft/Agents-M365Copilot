from enum import Enum

class AppleSubjectNameFormat(str, Enum):
    # Common name.
    CommonName = "commonName",
    # Common name as email.
    CommonNameAsEmail = "commonNameAsEmail",
    # Custom subject name format.
    Custom = "custom",
    # Common Name Including Email.
    CommonNameIncludingEmail = "commonNameIncludingEmail",
    # Common Name As IMEI.
    CommonNameAsIMEI = "commonNameAsIMEI",
    # Common Name As Serial Number.
    CommonNameAsSerialNumber = "commonNameAsSerialNumber",

