from enum import Enum

class WindowsHealthMonitoringScope(str, Enum):
    # Undefined
    Undefined = "undefined",
    # Basic events for windows device health monitoring
    HealthMonitoring = "healthMonitoring",
    # Boot performance events
    BootPerformance = "bootPerformance",
    # Windows updates events
    WindowsUpdates = "windowsUpdates",
    # PrivilegeManagement
    PrivilegeManagement = "privilegeManagement",

