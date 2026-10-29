from enum import Enum

class LanManagerAuthenticationLevel(str, Enum):
    # Send LM & NTLM responses
    LmAndNltm = "lmAndNltm",
    # Send LM & NTLM-use NTLMv2 session security if negotiated
    LmNtlmAndNtlmV2 = "lmNtlmAndNtlmV2",
    # Send LM & NTLM responses only
    LmAndNtlmOnly = "lmAndNtlmOnly",
    # Send LM & NTLMv2 responses only
    LmAndNtlmV2 = "lmAndNtlmV2",
    # Send LM & NTLMv2 responses only. Refuse LM
    LmNtlmV2AndNotLm = "lmNtlmV2AndNotLm",
    # Send LM & NTLMv2 responses only. Refuse LM & NTLM
    LmNtlmV2AndNotLmOrNtm = "lmNtlmV2AndNotLmOrNtm",

