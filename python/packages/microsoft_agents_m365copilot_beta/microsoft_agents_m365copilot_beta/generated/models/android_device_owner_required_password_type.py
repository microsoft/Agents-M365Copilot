from enum import Enum

class AndroidDeviceOwnerRequiredPasswordType(str, Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # There must be a password set, but there are no restrictions on type.
    Required = "required",
    # At least numeric.
    Numeric = "numeric",
    # At least numeric with no repeating or ordered sequences.
    NumericComplex = "numericComplex",
    # At least alphabetic password.
    Alphabetic = "alphabetic",
    # At least alphanumeric password
    Alphanumeric = "alphanumeric",
    # At least alphanumeric with symbols.
    AlphanumericWithSymbols = "alphanumericWithSymbols",
    # Low security biometrics based password required.
    LowSecurityBiometric = "lowSecurityBiometric",
    # Custom password set by the admin.
    CustomPassword = "customPassword",

