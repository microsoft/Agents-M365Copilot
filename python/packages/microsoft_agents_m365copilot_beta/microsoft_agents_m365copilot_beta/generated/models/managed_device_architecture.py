from enum import Enum

class ManagedDeviceArchitecture(str, Enum):
    # Unknown architecture
    Unknown = "unknown",
    # X86
    X86 = "x86",
    # X64
    X64 = "x64",
    # ARM
    Arm = "arm",
    # ARM64
    ArM64 = "arM64",

