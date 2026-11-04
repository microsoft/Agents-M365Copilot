from enum import Enum

class SpendingPolicyStatus(str, Enum):
    # The policy is active and enforced.
    Enabled = "enabled",
    # The policy is not enforced. This is the initial state of a newly created policy. A policyis also disabled when every group assigned to it has been deleted, or when the servicedisables it in response to a change in the tenant's subscription.
    Disabled = "disabled",
    # The policy is being created or transitioned; group links and validation are in progress.
    Provisioning = "provisioning",
    # The most recent provisioning attempt failed; the policy is not enforced.
    ProvisioningFailed = "provisioningFailed",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

