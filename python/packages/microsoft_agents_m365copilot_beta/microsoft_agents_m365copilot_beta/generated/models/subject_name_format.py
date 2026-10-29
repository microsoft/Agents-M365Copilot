from enum import Enum

class SubjectNameFormat(str, Enum):
    # Common name.
    CommonName = "commonName",
    # Common Name Including Email.
    CommonNameIncludingEmail = "commonNameIncludingEmail",
    # Common Name As Email.
    CommonNameAsEmail = "commonNameAsEmail",
    # Custom subject name format.
    Custom = "custom",
    # Common Name As IMEI.
    CommonNameAsIMEI = "commonNameAsIMEI",
    # Common Name As Serial Number.
    CommonNameAsSerialNumber = "commonNameAsSerialNumber",
    # Common Name As Serial Number.
    CommonNameAsAadDeviceId = "commonNameAsAadDeviceId",
    # Common Name As Serial Number.
    CommonNameAsIntuneDeviceId = "commonNameAsIntuneDeviceId",
    # Common Name As Serial Number.
    CommonNameAsDurableDeviceId = "commonNameAsDurableDeviceId",

