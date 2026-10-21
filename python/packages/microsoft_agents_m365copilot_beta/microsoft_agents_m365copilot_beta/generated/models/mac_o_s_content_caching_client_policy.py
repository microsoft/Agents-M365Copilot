from enum import Enum

class MacOSContentCachingClientPolicy(str, Enum):
    # Defaults to clients in local network.
    NotConfigured = "notConfigured",
    # Content caches will provide content to devices only in their immediate local network.
    ClientsInLocalNetwork = "clientsInLocalNetwork",
    # Content caches will provide content to devices that share the same public IP address.
    ClientsWithSamePublicIpAddress = "clientsWithSamePublicIpAddress",
    # Content caches will provide content to devices in contentCachingClientListenRanges.
    ClientsInCustomLocalNetworks = "clientsInCustomLocalNetworks",
    # Content caches will provide content to devices in contentCachingClientListenRanges, contentCachingPeerListenRanges, and contentCachingParents.
    ClientsInCustomLocalNetworksWithFallback = "clientsInCustomLocalNetworksWithFallback",

