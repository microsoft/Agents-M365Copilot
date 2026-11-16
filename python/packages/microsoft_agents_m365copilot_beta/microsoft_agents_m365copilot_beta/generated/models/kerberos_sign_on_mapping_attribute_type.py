from enum import Enum

class KerberosSignOnMappingAttributeType(str, Enum):
    UserPrincipalName = "userPrincipalName",
    OnPremisesUserPrincipalName = "onPremisesUserPrincipalName",
    UserPrincipalUsername = "userPrincipalUsername",
    OnPremisesUserPrincipalUsername = "onPremisesUserPrincipalUsername",
    OnPremisesSAMAccountName = "onPremisesSAMAccountName",

