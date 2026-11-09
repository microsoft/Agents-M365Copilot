from enum import Enum

class GroupPolicyDefinitionClassType(str, Enum):
    # Identifies placement of the policy setting under the user configuration node.
    User = "user",
    # Identifies placement of the policy setting under the computer configuration node.
    Machine = "machine",

