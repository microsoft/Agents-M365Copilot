from enum import Enum

class LocalSecurityOptionsMinimumSessionSecurity(str, Enum):
    # Send LM & NTLM responses
    None_ = "none",
    # Send LM & NTLM-use NTLMv2 session security if negotiated
    RequireNtmlV2SessionSecurity = "requireNtmlV2SessionSecurity",
    # Send LM & NTLM responses only
    Require128BitEncryption = "require128BitEncryption",
    # Send LM & NTLMv2 responses only
    NtlmV2And128BitEncryption = "ntlmV2And128BitEncryption",

