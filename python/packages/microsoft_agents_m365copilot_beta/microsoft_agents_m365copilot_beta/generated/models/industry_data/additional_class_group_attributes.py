from enum import Enum

class AdditionalClassGroupAttributes(str, Enum):
    CourseTitle = "courseTitle",
    CourseCode = "courseCode",
    CourseSubject = "courseSubject",
    CourseGradeLevel = "courseGradeLevel",
    CourseExternalId = "courseExternalId",
    AcademicSessionTitle = "academicSessionTitle",
    AcademicSessionExternalId = "academicSessionExternalId",
    ClassCode = "classCode",
    UnknownFutureValue = "unknownFutureValue",

