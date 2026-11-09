from enum import Enum

class EnrollmentNotificationTemplateType(str, Enum):
    # Email Notification
    Email = "email",
    # Push Notification
    Push = "push",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

