from enum import Enum

class IosWiredNetworkEapType(str, Enum):
    # EAP-Transport Layer Security (EAP-TLS).
    EapTls = "eapTls",
    # EAP-Tunneled Transport Layer Security (EAP-TTLS).
    EapTtls = "eapTtls",
    # Protected Extensible Authentication Protocol (PEAP).
    Peap = "peap",
    # EAP-Flexible Authentication via Secure Tunneling (EAP-FAST).
    EapFast = "eapFast",
    # EAP-Authentication and Key Agreement (EAP-AKA).
    EapAka = "eapAka",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

