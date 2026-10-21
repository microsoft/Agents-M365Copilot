from enum import Enum

class AndroidKeyguardFeature(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Camera usage when on secure keyguard screens.
    Camera = "camera",
    # Showing notifications when on secure keyguard screens.
    Notifications = "notifications",
    # Showing unredacted notifications when on secure keyguard screens.
    UnredactedNotifications = "unredactedNotifications",
    # Trust agent state when on secure keyguard screens.
    TrustAgents = "trustAgents",
    # Fingerprint sensor usage when on secure keyguard screens.
    Fingerprint = "fingerprint",
    # Notification text entry when on secure keyguard screens.
    RemoteInput = "remoteInput",
    # All keyguard features when on secure keyguard screens.
    AllFeatures = "allFeatures",
    # Face authentication on secure keyguard screens.
    Face = "face",
    # Iris authentication on secure keyguard screens.
    Iris = "iris",
    # All biometric authentication on secure keyguard screens.
    Biometrics = "biometrics",

