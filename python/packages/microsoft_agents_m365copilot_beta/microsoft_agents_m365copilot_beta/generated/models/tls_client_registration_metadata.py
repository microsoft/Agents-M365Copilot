from enum import Enum

class TlsClientRegistrationMetadata(str, Enum):
    Tls_client_auth_subject_dn = "tls_client_auth_subject_dn",
    Tls_client_auth_san_dns = "tls_client_auth_san_dns",
    Tls_client_auth_san_uri = "tls_client_auth_san_uri",
    Tls_client_auth_san_ip = "tls_client_auth_san_ip",
    Tls_client_auth_san_email = "tls_client_auth_san_email",
    UnknownFutureValue = "unknownFutureValue",

