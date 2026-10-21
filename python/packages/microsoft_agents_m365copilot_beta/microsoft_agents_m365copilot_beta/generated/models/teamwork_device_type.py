from enum import Enum

class TeamworkDeviceType(str, Enum):
    Unknown = "unknown",
    IpPhone = "ipPhone",
    TeamsRoom = "teamsRoom",
    SurfaceHub = "surfaceHub",
    CollaborationBar = "collaborationBar",
    TeamsDisplay = "teamsDisplay",
    TouchConsole = "touchConsole",
    LowCostPhone = "lowCostPhone",
    TeamsPanel = "teamsPanel",
    Sip = "sip",
    UnknownFutureValue = "unknownFutureValue",

