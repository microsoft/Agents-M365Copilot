from enum import Enum

class BookingInvoiceStatus(str, Enum):
    Draft = "draft",
    Reviewing = "reviewing",
    Open = "open",
    Canceled = "canceled",
    Paid = "paid",
    Corrective = "corrective",

