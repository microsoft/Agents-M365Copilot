from enum import Enum

class MigrationState(str, Enum):
    ReadyForMigration = "readyForMigration",
    NotReadyForMigration = "notReadyForMigration",
    UpToDate = "upToDate",
    MigrationFailed = "migrationFailed",
    Migrating = "migrating",
    UnknownFutureValue = "unknownFutureValue",

