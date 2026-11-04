from enum import Enum

class UpdateClassification(str, Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Recommended and important.
    RecommendedAndImportant = "recommendedAndImportant",
    # Important.
    Important = "important",
    # None.
    None_ = "none",

