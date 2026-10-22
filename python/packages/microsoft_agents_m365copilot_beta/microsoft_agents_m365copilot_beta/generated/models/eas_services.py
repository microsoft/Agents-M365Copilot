from enum import Enum

class EasServices(str, Enum):
    None_ = "none",
    # Enables synchronization of calendars.
    Calendars = "calendars",
    # Enables synchronization of contacts.
    Contacts = "contacts",
    # Enables synchronization of email.
    Email = "email",
    # Enables synchronization of notes.
    Notes = "notes",
    # Enables synchronization of reminders.
    Reminders = "reminders",

