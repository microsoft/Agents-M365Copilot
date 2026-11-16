from enum import Enum

class MessagingRedirectAppType(str, Enum):
    # App protection policy will allow messaging redirection to any app.
    AnyApp = "anyApp",
    # App protection policy will allow messaging redirection to any managed application.
    AnyManagedApp = "anyManagedApp",
    # App protection policy will allow messaging redirection only to specified applications in related App protection policy settings. See related settings `messagingRedirectAppDisplayName`, `messagingRedirectAppPackageId` and `messagingRedirectAppUrlScheme`.
    SpecificApps = "specificApps",
    # App protection policy will block messaging redirection to any app.
    Blocked = "blocked",

