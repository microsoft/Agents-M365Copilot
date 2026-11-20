from enum import Enum

class MeetingCopilotMode(str, Enum):
    # Copilot is on.
    Enabled = "enabled",
    # Copilot is on and a saved transcript is required.
    EnabledWithTranscript = "enabledWithTranscript",
    # Copilot is on and the transcript is saved by default.
    EnabledWithTranscriptDefaultOn = "enabledWithTranscriptDefaultOn",
    # Copilot is off.
    Disabled = "disabled",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

