from enum import Enum

class IosWallpaperDisplayLocation(str, Enum):
    # No location specified for wallpaper display.
    NotConfigured = "notConfigured",
    # A configured wallpaper image is displayed on Lock screen.
    LockScreen = "lockScreen",
    # A configured wallpaper image is displayed on Home (icon list) screen.
    HomeScreen = "homeScreen",
    # A configured wallpaper image is displayed on Lock screen and Home screen.
    LockAndHomeScreens = "lockAndHomeScreens",

