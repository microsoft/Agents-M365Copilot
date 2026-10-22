from enum import Enum

class EapFastConfiguration(str, Enum):
    # Use EAP-FAST without Protected Access Credential (PAC).
    NoProtectedAccessCredential = "noProtectedAccessCredential",
    # Use Protected Access Credential (PAC).
    UseProtectedAccessCredential = "useProtectedAccessCredential",
    # Use Protected Access Credential (PAC) and Provision PAC.
    UseProtectedAccessCredentialAndProvision = "useProtectedAccessCredentialAndProvision",
    # Use Protected Access Credential (PAC), Provision PAC, and do so anonymously.
    UseProtectedAccessCredentialAndProvisionAnonymously = "useProtectedAccessCredentialAndProvisionAnonymously",

