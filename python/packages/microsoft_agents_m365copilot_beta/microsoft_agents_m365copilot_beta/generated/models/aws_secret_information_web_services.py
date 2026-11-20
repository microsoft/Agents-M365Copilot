from enum import Enum

class AwsSecretInformationWebServices(str, Enum):
    SecretsManager = "secretsManager",
    CertificateAuthority = "certificateAuthority",
    CloudHsm = "cloudHsm",
    CertificateManager = "certificateManager",
    UnknownFutureValue = "unknownFutureValue",

