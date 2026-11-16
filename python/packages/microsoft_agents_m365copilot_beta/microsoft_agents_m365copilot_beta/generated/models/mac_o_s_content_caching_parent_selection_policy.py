from enum import Enum

class MacOSContentCachingParentSelectionPolicy(str, Enum):
    # Defaults to round-robin strategy.
    NotConfigured = "notConfigured",
    # Rotate through the parents in order. Use this policy for load balancing.
    RoundRobin = "roundRobin",
    # Always use the first available parent in the Parents list. Use this policy to designate permanent primary, secondary, and subsequent parents.
    FirstAvailable = "firstAvailable",
    # Hash the path part of the requested URL so that the same parent is always used for the same URL. This is useful for maximizing the size of the combined caches of the parents.
    UrlPathHash = "urlPathHash",
    # Choose a parent at random. Use this policy for load balancing.
    Random = "random",
    # Use the first available parent that is available in the Parents list until it becomes unavailable, then advance to the next one. Use this policy for designating floating primary, secondary, and subsequent parents.
    StickyAvailable = "stickyAvailable",

