from enum import Enum

class MacOSContentCachingType(str, Enum):
    # Default. Both user iCloud data and non-iCloud data will be cached.
    NotConfigured = "notConfigured",
    # Allow Apple's content caching service to cache user iCloud data.
    UserContentOnly = "userContentOnly",
    # Allow Apple's content caching service to cache non-iCloud data (e.g. app and software updates).
    SharedContentOnly = "sharedContentOnly",

