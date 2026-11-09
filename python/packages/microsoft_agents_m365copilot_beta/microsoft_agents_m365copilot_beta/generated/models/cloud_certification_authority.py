from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_certification_authority_certificate_key_size import CloudCertificationAuthorityCertificateKeySize
    from .cloud_certification_authority_hashing_algorithm import CloudCertificationAuthorityHashingAlgorithm
    from .cloud_certification_authority_key_platform_type import CloudCertificationAuthorityKeyPlatformType
    from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
    from .cloud_certification_authority_status import CloudCertificationAuthorityStatus
    from .cloud_certification_authority_type import CloudCertificationAuthorityType
    from .cloud_certification_authority_version import CloudCertificationAuthorityVersion
    from .entity import Entity
    from .extended_key_usage import ExtendedKeyUsage

from .entity import Entity

@dataclass
class CloudCertificationAuthority(Entity, Parsable):
    """
    Entity that represents a collection of metadata of a cloud certification authority.
    """
    # The currently active certification authority version. This navigation property provides direct access to the active version's details including certificate information, URLs, and validity periods. The active version is automatically included in the default response when retrieving a certification authority entity without requiring $expand. Read-only.
    active_version: Optional[CloudCertificationAuthorityVersion] = None
    # The URL to download the certification authority certificate. Read-only.
    certificate_download_url: Optional[str] = None
    # Enum of possible cloud certification authority certificate cryptography and key size combinations.
    certificate_key_size: Optional[CloudCertificationAuthorityCertificateKeySize] = None
    # The cloud certification authority's Certificate Revocation List URL that can be used to determine revocation status. Read-only.
    certificate_revocation_list_url: Optional[str] = None
    # The certificate signing request used to create an issuing certification authority with a root certification authority external to Microsoft Cloud PKI. The based-64 encoded certificate signing request can be downloaded through this property. After downloading the certificate signing request, it must be signed by the external root certifcation authority. Read-only.
    certificate_signing_request: Optional[str] = None
    # Issuer (parent) certification authority identifier. Nullable. Read-only. Supports $orderby and $select.
    certification_authority_issuer_id: Optional[str] = None
    # The URI of the issuing certification authority of a subordinate certification authority. Returns null if a root certification authority. Nullable. Read-only.
    certification_authority_issuer_uri: Optional[str] = None
    # Enum type of possible certification authority statuses. These statuses indicate whether a certification authority is currently able to issue certificates, temporarily paused, pending signing, revoked, or expired.
    certification_authority_status: Optional[CloudCertificationAuthorityStatus] = None
    # Enum type of possible certificate hashing algorithms used by the certification authority to create certificates.
    cloud_certification_authority_hashing_algorithm: Optional[CloudCertificationAuthorityHashingAlgorithm] = None
    # Required OData property to expose leaf certificate API.
    cloud_certification_authority_leaf_certificate: Optional[list[CloudCertificationAuthorityLeafCertificate]] = None
    # Enum type of possible certificate authority types. This feature supports a two-tier certification authority model with a root certification authority and one or more child issuing (intermediate) certification authorities.
    cloud_certification_authority_type: Optional[CloudCertificationAuthorityType] = None
    # The common name of the certificate subject name, which must be unique. This property is a relative distinguished name used to compose the certificate subject name. Read-only. Supports $select.
    common_name: Optional[str] = None
    # The country name that is used to compose the subject name of a certification authority certificate in the form 'C='. Nullable. Example: US. Read-only.
    country_name: Optional[str] = None
    # Creation date of this cloud certification authority entity instance. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The certification authority description displayed in the Intune admin console. Nullable. Read/write. Returns null if not set.
    description: Optional[str] = None
    # The certification authority display name the Intune admin console. Read/write. Supports $select and $orderby.
    display_name: Optional[str] = None
    # ETag for optimistic concurrency control. Read/write.
    e_tag: Optional[str] = None
    # The certificate extended key usages, which specify the usage capabilities of the certificate. Read-only.
    extended_key_usages: Optional[list[ExtendedKeyUsage]] = None
    # The geographic region where a cloud certification authority (CA) is hosted. Read-only.
    geographic_region: Optional[str] = None
    # The issuerCommonName property
    issuer_common_name: Optional[str] = None
    # Enum type of possible key platforms used by the certification authority.
    key_platform: Optional[CloudCertificationAuthorityKeyPlatformType] = None
    # Last modification date and time of this certification authority entity instance. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read/write.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The locality (town, city, etc.) name that is used to compose the subject name of a certification authority certificate in the form 'L='. This is Nullable. Example: Redmond. Read-only.
    locality_name: Optional[str] = None
    # The Online Certificate Status Protocol (OCSP) responder URI that can be used to determine certificate status. Read-only.
    ocsp_responder_uri: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organization name that is used as a distinguished name in the subject name of a certification authority certificate in the form 'O='. Nullable. Example: Microsoft. Read-only.
    organization_name: Optional[str] = None
    # The organization unit name that is used as a distinguished name in the subject name of a certification authority certificate in the form 'OU='. Nullable. Example: Security. Read-only.
    organization_unit: Optional[str] = None
    # List of Scope Tags for this entity instance. Scope tags limit access to an entity instance. Nullable. Read/write.
    role_scope_tag_ids: Optional[list[str]] = None
    # The common name of the certificate subject name of the certification authority issuer. This property can be used to identify the certification authority that issued the current certification authority. For issuing certification authorities, this is the common name of the certificate subject name of the root certification authority to which it is anchored. For externally signed certification authorities, this is the common name of the certificate subject name of the signing certification authority. For root certification authorities, this is the common name of the certification authority's own certificate subject name. Read-only.
    root_certificate_common_name: Optional[str] = None
    # The SCEP server URL for device SCEP connections to request certificates. Read-only.
    scep_server_url: Optional[str] = None
    # The serial number used to uniquely identify a certificate with its issuing certification authority. Read-only. Supports $select.
    serial_number: Optional[str] = None
    # The state or province name that is used to compose the subject name of a certification authority certificate in the form 'ST='. Nullable. Example: Washington. Read-only.
    state_name: Optional[str] = None
    # The subject name of the certificate. The subject is the target or intended beneficiary of the security being provided, such as a company or government entity. Read-only. Supports $orderby and $select.
    subject_name: Optional[str] = None
    # Secure Hash Algorithm 1 digest of the certificate that can be used to identify it. Read-only. Supports $select.
    thumbprint: Optional[str] = None
    # The end date time of the validity period of a certification authority certificate. Certificates cannot be used after this date time as they are longer valid. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only. Supports $orderby.
    validity_end_date_time: Optional[datetime.datetime] = None
    # The certification authority validity period in years configured by admins.
    validity_period_in_years: Optional[int] = None
    # The start date time of the validity period of a certification authority certificate. Certificates cannot be used before this date time as they are not yet valid. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Nullable. Read-only. Supports $orderby.
    validity_start_date_time: Optional[datetime.datetime] = None
    # The certification authority version, which is incremented each time the certification authority is renewed. Read-only.
    version_number: Optional[int] = None
    # The collection of all certification authority versions, including active, staged, retired, and expired versions. This navigation property provides access to the full version history of the certification authority. Use $expand=versions to include this collection in the response. Read-only.
    versions: Optional[list[CloudCertificationAuthorityVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudCertificationAuthority:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudCertificationAuthority
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudCertificationAuthority()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_certification_authority_certificate_key_size import CloudCertificationAuthorityCertificateKeySize
        from .cloud_certification_authority_hashing_algorithm import CloudCertificationAuthorityHashingAlgorithm
        from .cloud_certification_authority_key_platform_type import CloudCertificationAuthorityKeyPlatformType
        from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
        from .cloud_certification_authority_status import CloudCertificationAuthorityStatus
        from .cloud_certification_authority_type import CloudCertificationAuthorityType
        from .cloud_certification_authority_version import CloudCertificationAuthorityVersion
        from .entity import Entity
        from .extended_key_usage import ExtendedKeyUsage

        from .cloud_certification_authority_certificate_key_size import CloudCertificationAuthorityCertificateKeySize
        from .cloud_certification_authority_hashing_algorithm import CloudCertificationAuthorityHashingAlgorithm
        from .cloud_certification_authority_key_platform_type import CloudCertificationAuthorityKeyPlatformType
        from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
        from .cloud_certification_authority_status import CloudCertificationAuthorityStatus
        from .cloud_certification_authority_type import CloudCertificationAuthorityType
        from .cloud_certification_authority_version import CloudCertificationAuthorityVersion
        from .entity import Entity
        from .extended_key_usage import ExtendedKeyUsage

        fields: dict[str, Callable[[Any], None]] = {
            "activeVersion": lambda n : setattr(self, 'active_version', n.get_object_value(CloudCertificationAuthorityVersion)),
            "certificateDownloadUrl": lambda n : setattr(self, 'certificate_download_url', n.get_str_value()),
            "certificateKeySize": lambda n : setattr(self, 'certificate_key_size', n.get_enum_value(CloudCertificationAuthorityCertificateKeySize)),
            "certificateRevocationListUrl": lambda n : setattr(self, 'certificate_revocation_list_url', n.get_str_value()),
            "certificateSigningRequest": lambda n : setattr(self, 'certificate_signing_request', n.get_str_value()),
            "certificationAuthorityIssuerId": lambda n : setattr(self, 'certification_authority_issuer_id', n.get_str_value()),
            "certificationAuthorityIssuerUri": lambda n : setattr(self, 'certification_authority_issuer_uri', n.get_str_value()),
            "certificationAuthorityStatus": lambda n : setattr(self, 'certification_authority_status', n.get_enum_value(CloudCertificationAuthorityStatus)),
            "cloudCertificationAuthorityHashingAlgorithm": lambda n : setattr(self, 'cloud_certification_authority_hashing_algorithm', n.get_enum_value(CloudCertificationAuthorityHashingAlgorithm)),
            "cloudCertificationAuthorityLeafCertificate": lambda n : setattr(self, 'cloud_certification_authority_leaf_certificate', n.get_collection_of_object_values(CloudCertificationAuthorityLeafCertificate)),
            "cloudCertificationAuthorityType": lambda n : setattr(self, 'cloud_certification_authority_type', n.get_enum_value(CloudCertificationAuthorityType)),
            "commonName": lambda n : setattr(self, 'common_name', n.get_str_value()),
            "countryName": lambda n : setattr(self, 'country_name', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "eTag": lambda n : setattr(self, 'e_tag', n.get_str_value()),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(ExtendedKeyUsage)),
            "geographicRegion": lambda n : setattr(self, 'geographic_region', n.get_str_value()),
            "issuerCommonName": lambda n : setattr(self, 'issuer_common_name', n.get_str_value()),
            "keyPlatform": lambda n : setattr(self, 'key_platform', n.get_enum_value(CloudCertificationAuthorityKeyPlatformType)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "localityName": lambda n : setattr(self, 'locality_name', n.get_str_value()),
            "ocspResponderUri": lambda n : setattr(self, 'ocsp_responder_uri', n.get_str_value()),
            "organizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "organizationUnit": lambda n : setattr(self, 'organization_unit', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "rootCertificateCommonName": lambda n : setattr(self, 'root_certificate_common_name', n.get_str_value()),
            "scepServerUrl": lambda n : setattr(self, 'scep_server_url', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "stateName": lambda n : setattr(self, 'state_name', n.get_str_value()),
            "subjectName": lambda n : setattr(self, 'subject_name', n.get_str_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
            "validityEndDateTime": lambda n : setattr(self, 'validity_end_date_time', n.get_datetime_value()),
            "validityPeriodInYears": lambda n : setattr(self, 'validity_period_in_years', n.get_int_value()),
            "validityStartDateTime": lambda n : setattr(self, 'validity_start_date_time', n.get_datetime_value()),
            "versionNumber": lambda n : setattr(self, 'version_number', n.get_int_value()),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(CloudCertificationAuthorityVersion)),
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
        writer.write_object_value("activeVersion", self.active_version)
        writer.write_str_value("certificateDownloadUrl", self.certificate_download_url)
        writer.write_enum_value("certificateKeySize", self.certificate_key_size)
        writer.write_str_value("certificateRevocationListUrl", self.certificate_revocation_list_url)
        writer.write_str_value("certificateSigningRequest", self.certificate_signing_request)
        writer.write_str_value("certificationAuthorityIssuerId", self.certification_authority_issuer_id)
        writer.write_str_value("certificationAuthorityIssuerUri", self.certification_authority_issuer_uri)
        writer.write_enum_value("certificationAuthorityStatus", self.certification_authority_status)
        writer.write_enum_value("cloudCertificationAuthorityHashingAlgorithm", self.cloud_certification_authority_hashing_algorithm)
        writer.write_collection_of_object_values("cloudCertificationAuthorityLeafCertificate", self.cloud_certification_authority_leaf_certificate)
        writer.write_enum_value("cloudCertificationAuthorityType", self.cloud_certification_authority_type)
        writer.write_str_value("commonName", self.common_name)
        writer.write_str_value("countryName", self.country_name)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("eTag", self.e_tag)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_str_value("geographicRegion", self.geographic_region)
        writer.write_str_value("issuerCommonName", self.issuer_common_name)
        writer.write_enum_value("keyPlatform", self.key_platform)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("localityName", self.locality_name)
        writer.write_str_value("ocspResponderUri", self.ocsp_responder_uri)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_str_value("organizationUnit", self.organization_unit)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_str_value("rootCertificateCommonName", self.root_certificate_common_name)
        writer.write_str_value("scepServerUrl", self.scep_server_url)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("stateName", self.state_name)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_datetime_value("validityEndDateTime", self.validity_end_date_time)
        writer.write_int_value("validityPeriodInYears", self.validity_period_in_years)
        writer.write_datetime_value("validityStartDateTime", self.validity_start_date_time)
        writer.write_int_value("versionNumber", self.version_number)
        writer.write_collection_of_object_values("versions", self.versions)
    

