from enum import Enum

class AndroidEapType(str, Enum):
    # Extensible Authentication Protocol-Transport Layer Security (EAP-TLS).
    EapTls = "eapTls",
    # Extensible Authentication Protocol-Tunneled Transport Layer Security (EAP-TTLS).
    EapTtls = "eapTtls",
    # Protected Extensible Authentication Protocol (PEAP).
    Peap = "peap",

