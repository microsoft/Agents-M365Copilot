from enum import Enum

class MicrosoftTunnelDeploymentMode(str, Enum):
    # Default. Indicates that the Tunnel containers are deployed standalone and in rootful mode.
    StandaloneRootful = "standaloneRootful",
    # Indicates that the Tunnel containers are deployed standalone and in rootless mode.
    StandaloneRootless = "standaloneRootless",
    # Indicates that the Tunnel containers are deployed as part of a pod and in rootful mode.
    PodRootful = "podRootful",
    # Indicates that the Tunnel containers are deployed as part of a pod and in rootless mode.
    PodRootless = "podRootless",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

