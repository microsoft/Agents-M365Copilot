from enum import Enum

class EnrollmentState(str, Enum):
    NotEnrolled = "notEnrolled",
    Enrolled = "enrolled",
    EnrolledWithPolicy = "enrolledWithPolicy",
    Enrolling = "enrolling",
    Unenrolling = "unenrolling",
    UnknownFutureValue = "unknownFutureValue",

