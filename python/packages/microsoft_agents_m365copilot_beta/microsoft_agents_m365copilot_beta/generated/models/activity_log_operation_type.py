from enum import Enum

class ActivityLogOperationType(str, Enum):
    BackupPolicyCreated = "backupPolicyCreated",
    BackupPolicyActivated = "backupPolicyActivated",
    BackupPolicyModified = "backupPolicyModified",
    BackupPolicyPaused = "backupPolicyPaused",
    BackupPolicyRenamed = "backupPolicyRenamed",
    DynamicRuleExecution = "dynamicRuleExecution",
    DynamicRuleDeletion = "dynamicRuleDeletion",
    ProtectionUnitLevelOffboarding = "protectionUnitLevelOffboarding",
    PolicyLevelOffboarding = "policyLevelOffboarding",
    RestoreTaskCreated = "restoreTaskCreated",
    RestoreTaskCompleted = "restoreTaskCompleted",
    UnknownFutureValue = "unknownFutureValue",

