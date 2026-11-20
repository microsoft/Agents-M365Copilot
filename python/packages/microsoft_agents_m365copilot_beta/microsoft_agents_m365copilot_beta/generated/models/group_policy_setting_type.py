from enum import Enum

class GroupPolicySettingType(str, Enum):
    # GroupPolicySettingType unknown
    Unknown = "unknown",
    # Policy setting type
    Policy = "policy",
    # Account setting type
    Account = "account",
    # SecurityOptions setting type
    SecurityOptions = "securityOptions",
    # UserRightsAssignment setting type
    UserRightsAssignment = "userRightsAssignment",
    # AuditSetting setting type
    AuditSetting = "auditSetting",
    # WindowsFirewallSettings setting type
    WindowsFirewallSettings = "windowsFirewallSettings",
    # AppLockerRuleCollection setting type
    AppLockerRuleCollection = "appLockerRuleCollection",
    # DataSourcesSettings setting type
    DataSourcesSettings = "dataSourcesSettings",
    # DevicesSettings setting type
    DevicesSettings = "devicesSettings",
    # DriveMapSettings setting type
    DriveMapSettings = "driveMapSettings",
    # EnvironmentVariables setting type
    EnvironmentVariables = "environmentVariables",
    # FilesSettings setting type
    FilesSettings = "filesSettings",
    # FolderOptions setting type
    FolderOptions = "folderOptions",
    # Folders setting type
    Folders = "folders",
    # IniFiles setting type
    IniFiles = "iniFiles",
    # InternetOptions setting type
    InternetOptions = "internetOptions",
    # LocalUsersAndGroups setting type
    LocalUsersAndGroups = "localUsersAndGroups",
    # NetworkOptions setting type
    NetworkOptions = "networkOptions",
    # NetworkShares setting type
    NetworkShares = "networkShares",
    # NTServices setting type
    NtServices = "ntServices",
    # PowerOptions setting type
    PowerOptions = "powerOptions",
    # Printers setting type
    Printers = "printers",
    # RegionalOptionsSettings setting type
    RegionalOptionsSettings = "regionalOptionsSettings",
    # RegistrySettings setting type
    RegistrySettings = "registrySettings",
    # ScheduledTasks setting type
    ScheduledTasks = "scheduledTasks",
    # ShortcutSettings setting type
    ShortcutSettings = "shortcutSettings",
    # StartMenuSettings setting type
    StartMenuSettings = "startMenuSettings",

