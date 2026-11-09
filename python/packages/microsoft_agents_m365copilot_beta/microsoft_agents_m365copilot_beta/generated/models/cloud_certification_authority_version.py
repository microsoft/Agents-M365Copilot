from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_certification_authority_key_platform_type import CloudCertificationAuthorityKeyPlatformType
    from .cloud_certification_authority_version_status import CloudCertificationAuthorityVersionStatus
    from .cloud_certification_authority_version_usage import CloudCertificationAuthorityVersionUsage
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudCertificationAuthorityVersion(Entity, Parsable):
    """
    Entity that represents version-specific properties of a cloud certification authority.
    """
    # The URL to download the certification authority certificate. Read-only.
    certificate_download_url: Optional[str] = None
    # The cloud certification authority's Certificate Revocation List URL that can be used to determine revocation status. Read-only.
    certificate_revocation_list_url: Optional[str] = None
    # The certificate signing request used to create an issuing certification authority with a root certification authority external to Microsoft Cloud PKI. The based-64 encoded certificate signing request can be downloaded through this property. After downloading the certificate signing request, it must be signed by the external root certifcation authority. Read-only.
    certificate_signing_request: Optional[str] = None
    # The certification authority identifier. Read-only.
    certification_authority_id: Optional[str] = None
    # The URI of the issuing certification authority of a subordinate certification authority. Returns null if a root certification authority. Nullable. Read-only.
    certification_authority_issuer_uri: Optional[str] = None
    # Enum type of possible certification authority version statuses. These statuses indicate the lifecycle state of a certification authority version, including whether it is currently active, staged for renewal, retired, or in other states.
    certification_authority_version_status: Optional[CloudCertificationAuthorityVersionStatus] = None
    # The date and time when the certification authority version is scheduled to be decommissioned. Only applicable for staged certification authority versions. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only.
    decommission_date_time: Optional[datetime.datetime] = None
    # Enum type of possible key platforms used by the certification authority.
    key_platform: Optional[CloudCertificationAuthorityKeyPlatformType] = None
    # Last modification date and time of this certification authority entity instance. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The Online Certificate Status Protocol (OCSP) responder URI that can be used to determine certificate status. Read-only.
    ocsp_responder_uri: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The SCEP server URL for device SCEP connections to request certificates. Read-only.
    scep_server_url: Optional[str] = None
    # The serial number used to uniquely identify a certificate with its issuing certification authority. Read-only.
    serial_number: Optional[str] = None
    # The subject name of the certificate. The subject is the target or intended beneficiary of the security being provided, such as a company or government entity. Read-only.
    subject_name: Optional[str] = None
    # Secure Hash Algorithm 1 digest of the certificate that can be used to identify it. Read-only.
    thumbprint: Optional[str] = None
    # The usage details associated with this certification authority version, including reporting data such as the number of leaf certificates issued during the staged period. Read-only.
    usage: Optional[CloudCertificationAuthorityVersionUsage] = None
    # The end date time of the validity period of a certification authority certificate. Certificates cannot be used after this date time as they are longer valid. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only.
    validity_end_date_time: Optional[datetime.datetime] = None
    # The start date time of the validity period of a certification authority certificate. Certificates cannot be used before this date time as they are not yet valid. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only.
    validity_start_date_time: Optional[datetime.datetime] = None
    # The version number assigned to this specific certification authority version entity. Read-only.
    version_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudCertificationAuthorityVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudCertificationAuthorityVersion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudCertificationAuthorityVersion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_certification_authority_key_platform_type import CloudCertificationAuthorityKeyPlatformType
        from .cloud_certification_authority_version_status import CloudCertificationAuthorityVersionStatus
        from .cloud_certification_authority_version_usage import CloudCertificationAuthorityVersionUsage
        from .entity import Entity

        from .cloud_certification_authority_key_platform_type import CloudCertificationAuthorityKeyPlatformType
        from .cloud_certification_authority_version_status import CloudCertificationAuthorityVersionStatus
        from .cloud_certification_authority_version_usage import CloudCertificationAuthorityVersionUsage
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "certificateDownloadUrl": lambda n : setattr(self, 'certificate_download_url', n.get_str_value()),
            "certificateRevocationListUrl": lambda n : setattr(self, 'certificate_revocation_list_url', n.get_str_value()),
            "certificateSigningRequest": lambda n : setattr(self, 'certificate_signing_request', n.get_str_value()),
            "certificationAuthorityId": lambda n : setattr(self, 'certification_authority_id', n.get_str_value()),
            "certificationAuthorityIssuerUri": lambda n : setattr(self, 'certification_authority_issuer_uri', n.get_str_value()),
            "certificationAuthorityVersionStatus": lambda n : setattr(self, 'certification_authority_version_status', n.get_enum_value(CloudCertificationAuthorityVersionStatus)),
            "decommissionDateTime": lambda n : setattr(self, 'decommission_date_time', n.get_datetime_value()),
            "keyPlatform": lambda n : setattr(self, 'key_platform', n.get_enum_value(CloudCertificationAuthorityKeyPlatformType)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "ocspResponderUri": lambda n : setattr(self, 'ocsp_responder_uri', n.get_str_value()),
            "scepServerUrl": lambda n : setattr(self, 'scep_server_url', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "subjectName": lambda n : setattr(self, 'subject_name', n.get_str_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
            "usage": lambda n : setattr(self, 'usage', n.get_object_value(CloudCertificationAuthorityVersionUsage)),
            "validityEndDateTime": lambda n : setattr(self, 'validity_end_date_time', n.get_datetime_value()),
            "validityStartDateTime": lambda n : setattr(self, 'validity_start_date_time', n.get_datetime_value()),
            "versionNumber": lambda n : setattr(self, 'version_number', n.get_int_value()),
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
        writer.write_str_value("certificateDownloadUrl", self.certificate_download_url)
        writer.write_str_value("certificateRevocationListUrl", self.certificate_revocation_list_url)
        writer.write_str_value("certificateSigningRequest", self.certificate_signing_request)
        writer.write_str_value("certificationAuthorityId", self.certification_authority_id)
        writer.write_str_value("certificationAuthorityIssuerUri", self.certification_authority_issuer_uri)
        writer.write_enum_value("certificationAuthorityVersionStatus", self.certification_authority_version_status)
        writer.write_datetime_value("decommissionDateTime", self.decommission_date_time)
        writer.write_enum_value("keyPlatform", self.key_platform)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("ocspResponderUri", self.ocsp_responder_uri)
        writer.write_str_value("scepServerUrl", self.scep_server_url)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_object_value("usage", self.usage)
        writer.write_datetime_value("validityEndDateTime", self.validity_end_date_time)
        writer.write_datetime_value("validityStartDateTime", self.validity_start_date_time)
        writer.write_int_value("versionNumber", self.version_number)
    

