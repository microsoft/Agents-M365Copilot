from enum import Enum

class EapType(str, Enum):
    # EAP-Transport Layer Security (EAP-TLS).
    EapTls = "eapTls",
    # Lightweight Extensible Authentication Protocol (LEAP).
    Leap = "leap",
    # EAP for GSM Subscriber Identity Module (EAP-SIM).
    EapSim = "eapSim",
    # EAP-Tunneled Transport Layer Security (EAP-TTLS).
    EapTtls = "eapTtls",
    # Protected Extensible Authentication Protocol (PEAP).
    Peap = "peap",
    # EAP-Flexible Authentication via Secure Tunneling (EAP-FAST).
    EapFast = "eapFast",
    # Tunnel Extensible Authentication Protocol (TEAP).
    Teap = "teap",

