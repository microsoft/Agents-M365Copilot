from enum import Enum

class DefenderRealtimeScanDirection(str, Enum):
    # 0 (default) – Monitor all files(bi-directional)
    MonitorAllFiles = "monitorAllFiles",
    # Monitor incoming files only.
    MonitorIncomingFilesOnly = "monitorIncomingFilesOnly",
    # Monitor outgoing files only.
    MonitorOutgoingFilesOnly = "monitorOutgoingFilesOnly",

