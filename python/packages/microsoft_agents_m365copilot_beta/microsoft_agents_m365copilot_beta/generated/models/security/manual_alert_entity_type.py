from enum import Enum

class ManualAlertEntityType(str, Enum):
    User = "user",
    Device = "device",
    File = "file",
    Ip = "ip",
    Url = "url",
    CloudApplication = "cloudApplication",
    Mailbox = "mailbox",
    SecurityGroup = "securityGroup",
    AzureResource = "azureResource",
    AmazonResource = "amazonResource",
    GoogleCloudResource = "googleCloudResource",
    OAuthApplication = "oAuthApplication",
    EmailMessage = "emailMessage",
    EmailCluster = "emailCluster",
    Process = "process",
    RegistryKey = "registryKey",
    RegistryValue = "registryValue",
    UnknownFutureValue = "unknownFutureValue",

