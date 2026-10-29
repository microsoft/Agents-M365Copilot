from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_validity_period_scale import CertificateValidityPeriodScale

@dataclass
class IosEduCertificateSettings(AdditionalDataHolder, Parsable):
    """
    Trusted Root and PFX certificates for iOS EDU.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # File name to display in UI.
    cert_file_name: Optional[str] = None
    # PKCS Certificate Template Name.
    certificate_template_name: Optional[str] = None
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period.
    certificate_validity_period_value: Optional[int] = None
    # PKCS Certification Authority.
    certification_authority: Optional[str] = None
    # PKCS Certification Authority Name.
    certification_authority_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Certificate renewal threshold percentage. Valid values 1 to 99
    renewal_threshold_percentage: Optional[int] = None
    # Trusted Root Certificate.
    trusted_root_certificate: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosEduCertificateSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosEduCertificateSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosEduCertificateSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_validity_period_scale import CertificateValidityPeriodScale

        from .certificate_validity_period_scale import CertificateValidityPeriodScale

        fields: dict[str, Callable[[Any], None]] = {
            "certFileName": lambda n : setattr(self, 'cert_file_name', n.get_str_value()),
            "certificateTemplateName": lambda n : setattr(self, 'certificate_template_name', n.get_str_value()),
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "certificationAuthority": lambda n : setattr(self, 'certification_authority', n.get_str_value()),
            "certificationAuthorityName": lambda n : setattr(self, 'certification_authority_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "trustedRootCertificate": lambda n : setattr(self, 'trusted_root_certificate', n.get_bytes_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("certFileName", self.cert_file_name)
        writer.write_str_value("certificateTemplateName", self.certificate_template_name)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_str_value("certificationAuthority", self.certification_authority)
        writer.write_str_value("certificationAuthorityName", self.certification_authority_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_bytes_value("trustedRootCertificate", self.trusted_root_certificate)
        writer.write_additional_data_value(self.additional_data)
    

