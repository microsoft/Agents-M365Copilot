from enum import Enum

class ManagedDeviceWindowsOperatingSystemEditionType(str, Enum):
    # Default. Indicates Professional Operating System edition used for the managed device.
    Professional = "professional",
    # Indicates Professional N Operating System edition used for the managed device.
    ProfessionalN = "professionalN",
    # Indicates Enterprise Operating System edition used for the managed device.
    Enterprise = "enterprise",
    # Indicates Enterprise N Operating System edition used for the managed device.
    EnterpriseN = "enterpriseN",
    # Indicates Education Operating System edition used for the managed device.
    Education = "education",
    # Indicates Education N Operating System edition used for the managed device.
    EducationN = "educationN",
    # Indicates Pro Education Operating System edition used for the managed device.
    ProEducation = "proEducation",
    # Indicates Pro Education N Operating System edition used for the managed device.
    ProEducationN = "proEducationN",
    # Indicates Pro Workstation Operating System edition used for the managed device.
    ProWorkstation = "proWorkstation",
    # Indicates Pro Workstation N Operating System edition used for the managed device.
    ProWorkstationN = "proWorkstationN",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

