from enum import Enum

class EnvironmentKind(str, Enum):
    # An Azure subscription.
    AzureSubscription = "azureSubscription",
    # An AWS organization.
    AwsOrganization = "awsOrganization",
    # An AWS account.
    AwsAccount = "awsAccount",
    # A GCP organization.
    GcpOrganization = "gcpOrganization",
    # A GCP project.
    GcpProject = "gcpProject",
    # A Docker Hub organization.
    DockersHubOrganization = "dockersHubOrganization",
    # A DevOps connection.
    DevOpsConnection = "devOpsConnection",
    # An Azure DevOps organization.
    AzureDevOpsOrganization = "azureDevOpsOrganization",
    # A GitHub organization.
    GitHubOrganization = "gitHubOrganization",
    # A GitLab group.
    GitLabGroup = "gitLabGroup",
    # A JFrog Artifactory instance.
    JFrogArtifactory = "jFrogArtifactory",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

