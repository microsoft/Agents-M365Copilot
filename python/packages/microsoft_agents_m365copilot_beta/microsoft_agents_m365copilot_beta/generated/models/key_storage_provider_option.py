from enum import Enum

class KeyStorageProviderOption(str, Enum):
    # Import to Trusted Platform Module (TPM) KSP if present, otherwise import to Software KSP.
    UseTpmKspOtherwiseUseSoftwareKsp = "useTpmKspOtherwiseUseSoftwareKsp",
    # Import to Trusted Platform Module (TPM) KSP if present, otherwise fail.
    UseTpmKspOtherwiseFail = "useTpmKspOtherwiseFail",
    # Import to Passport for work KSP if available, otherwise fail.
    UsePassportForWorkKspOtherwiseFail = "usePassportForWorkKspOtherwiseFail",
    # Import to Software KSP.
    UseSoftwareKsp = "useSoftwareKsp",

