from enum import Enum

class WindowsPrivacyDataCategory(str, Enum):
    # No access level specified, no intents. Device may behave either as in UserInControl or ForceAllow. It may depend on the privacy data been accessed, Windows versions and other factors.
    NotConfigured = "notConfigured",
    # Let apps access user’s name, picture and other account information created in Microsoft account. Added in Windows 10, version 1607.
    AccountInfo = "accountInfo",
    # Allow apps to receive information, send notifications, and stay up-to-date, even when the user is not using them. Be aware that when disabling communication apps (Email, Voice, etc) from background access these apps may or may not function as they are with the background access. Added in Windows 10, version 1703.
    AppsRunInBackground = "appsRunInBackground",
    # Let apps access user’s calendar. Added in Windows 10, version 1607.
    Calendar = "calendar",
    # Let apps access user’s call history. Added in Windows 10, version 1607.
    CallHistory = "callHistory",
    # Let apps access the camera on user’s device. Added in Windows 10, version 1607.
    Camera = "camera",
    # Let apps access user’s contact information. Added in Windows 10, version 1607.
    Contacts = "contacts",
    # Let apps access diagnostic information about other running apps. Added in Windows 10, version 1703.
    DiagnosticsInfo = "diagnosticsInfo",
    # Let apps access and send email. Added in Windows 10, version 1607.
    Email = "email",
    # Let apps access the precise location data of device user. Added in Windows 10, version 1607.
    Location = "location",
    # Let apps read or send messages, text or MMS. Added in Windows 10, version 1607.
    Messaging = "messaging",
    # Let apps use microphone on the user device. Added in Windows 10, version 1607.
    Microphone = "microphone",
    # Let apps use motion data generated on the device user. Added in Windows 10, version 1607.
    Motion = "motion",
    # Let apps access user’s notifications. Added in Windows 10, version 1607.
    Notifications = "notifications",
    # Let apps access phone data and make phone calls. Added in Windows 10, version 1607.
    Phone = "phone",
    # Let apps use radios, including Bluetooth, to send and receive data. Added in Windows 10, version 1607.
    Radios = "radios",
    # Let apps access Task Scheduler. Added in Windows 10, version 1703.
    Tasks = "tasks",
    # Let apps automatically share and sync info with wireless devices that don’t explicitly pair with user’s device. Added in Windows 10, version 1607.
    SyncWithDevices = "syncWithDevices",
    # Let apps access trusted devices. Added in Windows 10, version 1607.
    TrustedDevices = "trustedDevices",

