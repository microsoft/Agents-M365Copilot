from enum import Enum

class ZebraFotaDeploymentState(str, Enum):
    # Deployment is created but Zebra has not confirmed its creation.
    PendingCreation = "pendingCreation",
    # Deployment was not successfully created with Zebra.
    CreateFailed = "createFailed",
    # Deployment has been created but has not been deployed yet.
    Created = "created",
    # Deployment has started but not completed.
    InProgress = "inProgress",
    # Deployment has completed or end date has passed.
    Completed = "completed",
    # Admin has requested to cancel a deployment but Zebra has not confirmed cancellation.
    PendingCancel = "pendingCancel",
    # Deployment has been successfully canceled by Zebra.
    Canceled = "canceled",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

