from enum import Enum

class AgentEndpointConfigurationType(str, Enum):
    ApiBased = "apiBased",
    BotBased = "botBased",
    UnknownFutureValue = "unknownFutureValue",

