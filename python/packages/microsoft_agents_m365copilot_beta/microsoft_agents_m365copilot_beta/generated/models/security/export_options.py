from enum import Enum

class ExportOptions(str, Enum):
    OriginalFiles = "originalFiles",
    Text = "text",
    PdfReplacement = "pdfReplacement",
    FileInfo = "fileInfo",
    Tags = "tags",
    UnknownFutureValue = "unknownFutureValue",
    SplitSource = "splitSource",
    IncludeFolderAndPath = "includeFolderAndPath",
    FriendlyName = "friendlyName",
    CondensePaths = "condensePaths",

