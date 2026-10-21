from enum import Enum

class WiredNetworkInterface(str, Enum):
    # Any Ethernet.
    AnyEthernet = "anyEthernet",
    # First active Ethernet.
    FirstActiveEthernet = "firstActiveEthernet",
    # Second active Ethernet.
    SecondActiveEthernet = "secondActiveEthernet",
    # Third active Ethernet.
    ThirdActiveEthernet = "thirdActiveEthernet",
    # First Ethernet.
    FirstEthernet = "firstEthernet",
    # Second Ethernet.
    SecondEthernet = "secondEthernet",
    # Third Ethernet.
    ThirdEthernet = "thirdEthernet",

