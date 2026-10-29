from enum import Enum

class ReceiverProtocol(str, Enum):
    Ftp = "ftp",
    Ftps = "ftps",
    SyslogUdp = "syslogUdp",
    SyslogTcp = "syslogTcp",
    SyslogTls = "syslogTls",
    UnknownFutureValue = "unknownFutureValue",

