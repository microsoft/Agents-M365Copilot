from enum import Enum

class SubmissionCategory(str, Enum):
    NotJunk = "notJunk",
    Spam = "spam",
    Phishing = "phishing",
    Malware = "malware",
    UnknownFutureValue = "unknownFutureValue",

