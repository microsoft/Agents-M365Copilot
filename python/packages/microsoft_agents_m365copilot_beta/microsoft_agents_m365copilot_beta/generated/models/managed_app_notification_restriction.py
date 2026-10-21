from enum import Enum

class ManagedAppNotificationRestriction(str, Enum):
    # Share all notifications.
    Allow = "allow",
    # Do not share Orgnizational data in notifications.
    BlockOrganizationalData = "blockOrganizationalData",
    # Do not share notifications.
    Block = "block",

