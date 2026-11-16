from enum import Enum

class ConnectorHealthCheckMetricName(str, Enum):
    # Measures connectivity between the connector and the Certificate Authority.
    CaConnectivity = "caConnectivity",
    # Measures whether the connector has the required Enroll permission on the certificate template for issuance.
    CaIssuancePermissions = "caIssuancePermissions",
    # Measures whether the connector has the required permissions to revoke certificates on the CA.
    CaRevocationPermissions = "caRevocationPermissions",
    # Measures whether the configured certificate template is valid and accessible.
    CertificateTemplate = "certificateTemplate",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

