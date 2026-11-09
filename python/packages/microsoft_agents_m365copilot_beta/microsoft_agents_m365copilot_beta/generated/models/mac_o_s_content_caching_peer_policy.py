from enum import Enum

class MacOSContentCachingPeerPolicy(str, Enum):
    # Defaults to peers in local network.
    NotConfigured = "notConfigured",
    # Content caches will only peer with caches in their immediate local network.
    PeersInLocalNetwork = "peersInLocalNetwork",
    # Content caches will only peer with caches that share the same public IP address.
    PeersWithSamePublicIpAddress = "peersWithSamePublicIpAddress",
    # Content caches will use contentCachingPeerFilterRanges and contentCachingPeerListenRanges to determine which caches to peer with.
    PeersInCustomLocalNetworks = "peersInCustomLocalNetworks",

