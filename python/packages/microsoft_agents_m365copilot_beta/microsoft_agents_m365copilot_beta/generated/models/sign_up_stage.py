from enum import Enum

class SignUpStage(str, Enum):
    CredentialCollection = "credentialCollection",
    CredentialValidation = "credentialValidation",
    CredentialFederation = "credentialFederation",
    Consent = "consent",
    AttributeCollectionAndValidation = "attributeCollectionAndValidation",
    UserCreation = "userCreation",
    TenantConsent = "tenantConsent",
    UnknownFutureValue = "unknownFutureValue",

