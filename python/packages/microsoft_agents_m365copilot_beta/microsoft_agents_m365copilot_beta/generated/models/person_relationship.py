from enum import Enum

class PersonRelationship(str, Enum):
    Manager = "manager",
    Colleague = "colleague",
    DirectReport = "directReport",
    DotLineReport = "dotLineReport",
    Assistant = "assistant",
    DotLineManager = "dotLineManager",
    AlternateContact = "alternateContact",
    Friend = "friend",
    Spouse = "spouse",
    Sibling = "sibling",
    Child = "child",
    Parent = "parent",
    Sponsor = "sponsor",
    EmergencyContact = "emergencyContact",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

