from enum import Enum

class ExpirationRequirement(str, Enum):
    RememberMultifactorAuthenticationOnTrustedDevices = "rememberMultifactorAuthenticationOnTrustedDevices",
    TenantTokenLifetimePolicy = "tenantTokenLifetimePolicy",
    AudienceTokenLifetimePolicy = "audienceTokenLifetimePolicy",
    SignInFrequencyPeriodicReauthentication = "signInFrequencyPeriodicReauthentication",
    NgcMfa = "ngcMfa",
    SignInFrequencyEveryTime = "signInFrequencyEveryTime",
    UnknownFutureValue = "unknownFutureValue",

