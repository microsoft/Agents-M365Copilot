from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_certification_authority_leaf_certificate_status import CloudCertificationAuthorityLeafCertificateStatus
    from .cloud_certification_authority_version import CloudCertificationAuthorityVersion
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudCertificationAuthorityLeafCertificate(Entity, Parsable):
    """
    Entity that represents a leaf certificate issued by a cloud certification authority.
    """
    # Enum type of possible leaf certificate statuses. These statuses indicate whether certificates are active and usable or unusable if they have been revoked or expired.
    certificate_status: Optional[CloudCertificationAuthorityLeafCertificateStatus] = None
    # The URI of the certification authority that issued the certificate. Read-only.
    certification_authority_issuer_uri: Optional[str] = None
    # The version number of the certification authority that issued this leaf certificate. Read-only.
    certification_authority_version_number: Optional[int] = None
    # The certification authority version that issued this leaf certificate. Read-only.
    cloud_certification_authority_version: Optional[CloudCertificationAuthorityVersion] = None
    # URL to find the relevant Certificate Revocation List for this certificate. Read-only.
    crl_distribution_point_url: Optional[str] = None
    # The unique identifier of the managed device for which the certificate was created. This ID is assigned at device enrollment time. Read-only. Supports $select.
    device_id: Optional[str] = None
    # Name of the device for which the certificate was created. Read-only. Supports $select.
    device_name: Optional[str] = None
    # The platform of the device for which the certificate was created. Possible values are: Android, AndroidForWork, iOS, MacOS, WindowsPhone81, Windows81AndLater, Windows10AndLater, AndroidWorkProfile, Unknown, AndroidAOSP, AndroidMobileApplicationManagement, iOSMobileApplicationManagement. Default value: Unknown. Read-only. Supports $select.
    device_platform: Optional[str] = None
    # Certificate extensions that further define the purpose of the public key contained in a certificate. Data is formatted as a comma-separated list of object identifiers (OID). For example a possible value is '1.3.6.1.5.5.7.3.2'. Read-only. Nullable.
    extended_key_usages: Optional[list[str]] = None
    # The globally unique identifier of the certification authority that issued the leaf certificate. Read-only.
    issuer_id: Optional[str] = None
    # The name of the certification authority that issued the leaf certificate. Read-only.
    issuer_name: Optional[str] = None
    # Certificate extensions that define the purpose of the public key contained in a certificate. For example possible values are 'Key Encipherment' and 'Digital Signature'. Read-only. Nullable.
    key_usages: Optional[list[str]] = None
    # The Online Certificate Status Protocol (OCSP) responder URI that can be used to determine certificate status. Read-only.
    ocsp_responder_uri: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time a certificate was revoked. If the certificate was not revoked, this will be null. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only.
    revocation_date_time: Optional[datetime.datetime] = None
    # The serial number used to uniquely identify a certificate with its issuing certification authority. Read-only. Supports $select.
    serial_number: Optional[str] = None
    # The subject name of the certificate. The subject is the target or intended beneficiary of the security being provided, such as a user or device. Read-only. Supports $select and $orderby.
    subject_name: Optional[str] = None
    # Secure Hash Algorithm 1 digest of the certificate that can be used to identify it. Read-only. Supports $select.
    thumbprint: Optional[str] = None
    # The unique identifier of the user for which the certificate was created. Null for userless devices. This is an Intune user ID. Nullable. Read-only. Supports $select.
    user_id: Optional[str] = None
    # User principal name of the user for which the certificate was created. Null for userless devices. Nullable. Read-only. Supports $select.
    user_principal_name: Optional[str] = None
    # The end date time of the validity period of a certificate. Certificates cannot be used after this date time as they are longer valid. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only. Supports $orderby.
    validity_end_date_time: Optional[datetime.datetime] = None
    # The start date time of the validity period of a certificate. Certificates cannot be used before this date time as they are not yet valid. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only. Supports $orderby.
    validity_start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudCertificationAuthorityLeafCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudCertificationAuthorityLeafCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudCertificationAuthorityLeafCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_certification_authority_leaf_certificate_status import CloudCertificationAuthorityLeafCertificateStatus
        from .cloud_certification_authority_version import CloudCertificationAuthorityVersion
        from .entity import Entity

        from .cloud_certification_authority_leaf_certificate_status import CloudCertificationAuthorityLeafCertificateStatus
        from .cloud_certification_authority_version import CloudCertificationAuthorityVersion
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "certificateStatus": lambda n : setattr(self, 'certificate_status', n.get_enum_value(CloudCertificationAuthorityLeafCertificateStatus)),
            "certificationAuthorityIssuerUri": lambda n : setattr(self, 'certification_authority_issuer_uri', n.get_str_value()),
            "certificationAuthorityVersionNumber": lambda n : setattr(self, 'certification_authority_version_number', n.get_int_value()),
            "cloudCertificationAuthorityVersion": lambda n : setattr(self, 'cloud_certification_authority_version', n.get_object_value(CloudCertificationAuthorityVersion)),
            "crlDistributionPointUrl": lambda n : setattr(self, 'crl_distribution_point_url', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "devicePlatform": lambda n : setattr(self, 'device_platform', n.get_str_value()),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_primitive_values(str)),
            "issuerId": lambda n : setattr(self, 'issuer_id', n.get_str_value()),
            "issuerName": lambda n : setattr(self, 'issuer_name', n.get_str_value()),
            "keyUsages": lambda n : setattr(self, 'key_usages', n.get_collection_of_primitive_values(str)),
            "ocspResponderUri": lambda n : setattr(self, 'ocsp_responder_uri', n.get_str_value()),
            "revocationDateTime": lambda n : setattr(self, 'revocation_date_time', n.get_datetime_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "subjectName": lambda n : setattr(self, 'subject_name', n.get_str_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "validityEndDateTime": lambda n : setattr(self, 'validity_end_date_time', n.get_datetime_value()),
            "validityStartDateTime": lambda n : setattr(self, 'validity_start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("certificateStatus", self.certificate_status)
        writer.write_str_value("certificationAuthorityIssuerUri", self.certification_authority_issuer_uri)
        writer.write_int_value("certificationAuthorityVersionNumber", self.certification_authority_version_number)
        writer.write_object_value("cloudCertificationAuthorityVersion", self.cloud_certification_authority_version)
        writer.write_str_value("crlDistributionPointUrl", self.crl_distribution_point_url)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("devicePlatform", self.device_platform)
        writer.write_collection_of_primitive_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_str_value("issuerId", self.issuer_id)
        writer.write_str_value("issuerName", self.issuer_name)
        writer.write_collection_of_primitive_values("keyUsages", self.key_usages)
        writer.write_str_value("ocspResponderUri", self.ocsp_responder_uri)
        writer.write_datetime_value("revocationDateTime", self.revocation_date_time)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_datetime_value("validityEndDateTime", self.validity_end_date_time)
        writer.write_datetime_value("validityStartDateTime", self.validity_start_date_time)
    

