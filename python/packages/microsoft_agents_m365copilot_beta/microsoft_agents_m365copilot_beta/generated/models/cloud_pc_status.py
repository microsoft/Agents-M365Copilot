from enum import Enum

class CloudPcStatus(str, Enum):
    NotProvisioned = "notProvisioned",
    Provisioning = "provisioning",
    Provisioned = "provisioned",
    InGracePeriod = "inGracePeriod",
    Deprovisioning = "deprovisioning",
    Failed = "failed",
    ProvisionedWithWarnings = "provisionedWithWarnings",
    Resizing = "resizing",
    Restoring = "restoring",
    PendingProvision = "pendingProvision",
    UnknownFutureValue = "unknownFutureValue",
    MovingRegion = "movingRegion",
    ResizePendingLicense = "resizePendingLicense",
    UpdatingSingleSignOn = "updatingSingleSignOn",
    ModifyingSingleSignOn = "modifyingSingleSignOn",
    RefreshPolicyConfiguration = "refreshPolicyConfiguration",
    Preparing = "preparing",
    FailoverInProgress = "failoverInProgress",
    FailbackInProgress = "failbackInProgress",

