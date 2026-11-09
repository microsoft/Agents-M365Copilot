from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .app_info_csa_star_level import AppInfoCsaStarLevel
    from .app_info_data_at_rest_encryption_method import AppInfoDataAtRestEncryptionMethod
    from .app_info_data_retention_policy import AppInfoDataRetentionPolicy
    from .app_info_encryption_protocol import AppInfoEncryptionProtocol
    from .app_info_fed_ramp_level import AppInfoFedRampLevel
    from .app_info_holding import AppInfoHolding
    from .app_info_pci_dss_version import AppInfoPciDssVersion
    from .app_info_uploaded_data_types import AppInfoUploadedDataTypes
    from .cloud_app_info_state import CloudAppInfoState

from ..entity import Entity

@dataclass
class DiscoveredCloudAppInfo(Entity, Parsable):
    # The csaStarLevel property
    csa_star_level: Optional[AppInfoCsaStarLevel] = None
    # The dataAtRestEncryptionMethod property
    data_at_rest_encryption_method: Optional[AppInfoDataAtRestEncryptionMethod] = None
    # Indicates the countries or regions in which your data center resides.
    data_center: Optional[str] = None
    # The dataRetentionPolicy property
    data_retention_policy: Optional[AppInfoDataRetentionPolicy] = None
    # Indicates the data types that an end user can upload to the app. The possible values are: documents, mediaFiles, codingFiles, creditCards, databaseFiles, none, unknown, unknownFutureValue.
    data_types: Optional[list[AppInfoUploadedDataTypes]] = None
    # Indicates the date when the app domain was registered.
    domain_registration_date_time: Optional[datetime.datetime] = None
    # The encryptionProtocol property
    encryption_protocol: Optional[AppInfoEncryptionProtocol] = None
    # The fedRampLevel property
    fed_ramp_level: Optional[AppInfoFedRampLevel] = None
    # Indicates the year that the specific app vendor was established.
    founded: Optional[int] = None
    # Indicates the GDPR readiness of the app in relation to policies app provides to safeguard personal user data.
    gdpr_readiness_statement: Optional[str] = None
    # Indicates the location of the headquarters of the app.
    headquarters: Optional[str] = None
    # The holding property
    holding: Optional[AppInfoHolding] = None
    # Indicates the company name that provides hosting services for the app.
    hosting_company: Optional[str] = None
    # The isAdminAuditTrail property
    is_admin_audit_trail: Optional[CloudAppInfoState] = None
    # The isCobitCompliant property
    is_cobit_compliant: Optional[CloudAppInfoState] = None
    # The isCoppaCompliant property
    is_coppa_compliant: Optional[CloudAppInfoState] = None
    # The isDataAuditTrail property
    is_data_audit_trail: Optional[CloudAppInfoState] = None
    # The isDataClassification property
    is_data_classification: Optional[CloudAppInfoState] = None
    # The isDataOwnership property
    is_data_ownership: Optional[CloudAppInfoState] = None
    # The isDisasterRecoveryPlan property
    is_disaster_recovery_plan: Optional[CloudAppInfoState] = None
    # The isDmca property
    is_dmca: Optional[CloudAppInfoState] = None
    # The isFerpaCompliant property
    is_ferpa_compliant: Optional[CloudAppInfoState] = None
    # The isFfiecCompliant property
    is_ffiec_compliant: Optional[CloudAppInfoState] = None
    # The isFileSharing property
    is_file_sharing: Optional[CloudAppInfoState] = None
    # The isFinraCompliant property
    is_finra_compliant: Optional[CloudAppInfoState] = None
    # The isFismaCompliant property
    is_fisma_compliant: Optional[CloudAppInfoState] = None
    # The isGaapCompliant property
    is_gaap_compliant: Optional[CloudAppInfoState] = None
    # The isGdprDataProtectionImpactAssessment property
    is_gdpr_data_protection_impact_assessment: Optional[CloudAppInfoState] = None
    # The isGdprDataProtectionOfficer property
    is_gdpr_data_protection_officer: Optional[CloudAppInfoState] = None
    # The isGdprDataProtectionSecureCrossBorderDataTransfer property
    is_gdpr_data_protection_secure_cross_border_data_transfer: Optional[CloudAppInfoState] = None
    # The isGdprImpactAssessment property
    is_gdpr_impact_assessment: Optional[CloudAppInfoState] = None
    # The isGdprLawfulBasisForProcessing property
    is_gdpr_lawful_basis_for_processing: Optional[CloudAppInfoState] = None
    # The isGdprReportDataBreaches property
    is_gdpr_report_data_breaches: Optional[CloudAppInfoState] = None
    # The isGdprRightToAccess property
    is_gdpr_right_to_access: Optional[CloudAppInfoState] = None
    # The isGdprRightToBeInformed property
    is_gdpr_right_to_be_informed: Optional[CloudAppInfoState] = None
    # The isGdprRightToDataPortablility property
    is_gdpr_right_to_data_portablility: Optional[CloudAppInfoState] = None
    # The isGdprRightToErasure property
    is_gdpr_right_to_erasure: Optional[CloudAppInfoState] = None
    # The isGdprRightToObject property
    is_gdpr_right_to_object: Optional[CloudAppInfoState] = None
    # The isGdprRightToRectification property
    is_gdpr_right_to_rectification: Optional[CloudAppInfoState] = None
    # The isGdprRightToRestrictionOfProcessing property
    is_gdpr_right_to_restriction_of_processing: Optional[CloudAppInfoState] = None
    # The isGdprRightsRelatedToAutomatedDecisionMaking property
    is_gdpr_rights_related_to_automated_decision_making: Optional[CloudAppInfoState] = None
    # The isGdprSecureCrossBorderDataControl property
    is_gdpr_secure_cross_border_data_control: Optional[CloudAppInfoState] = None
    # The isGlbaCompliant property
    is_glba_compliant: Optional[CloudAppInfoState] = None
    # The isHipaaCompliant property
    is_hipaa_compliant: Optional[CloudAppInfoState] = None
    # The isHitrustCsfCompliant property
    is_hitrust_csf_compliant: Optional[CloudAppInfoState] = None
    # The isHttpSecurityHeadersContentSecurityPolicy property
    is_http_security_headers_content_security_policy: Optional[CloudAppInfoState] = None
    # The isHttpSecurityHeadersStrictTransportSecurity property
    is_http_security_headers_strict_transport_security: Optional[CloudAppInfoState] = None
    # The isHttpSecurityHeadersXContentTypeOptions property
    is_http_security_headers_x_content_type_options: Optional[CloudAppInfoState] = None
    # The isHttpSecurityHeadersXFrameOptions property
    is_http_security_headers_x_frame_options: Optional[CloudAppInfoState] = None
    # The isHttpSecurityHeadersXXssProtection property
    is_http_security_headers_x_xss_protection: Optional[CloudAppInfoState] = None
    # The isIpAddressRestriction property
    is_ip_address_restriction: Optional[CloudAppInfoState] = None
    # The isIsae3402Compliant property
    is_isae3402_compliant: Optional[CloudAppInfoState] = None
    # The isIso27001Compliant property
    is_iso27001_compliant: Optional[CloudAppInfoState] = None
    # The isIso27017Compliant property
    is_iso27017_compliant: Optional[CloudAppInfoState] = None
    # The isIso27018Compliant property
    is_iso27018_compliant: Optional[CloudAppInfoState] = None
    # The isItarCompliant property
    is_itar_compliant: Optional[CloudAppInfoState] = None
    # The isMultiFactorAuthentication property
    is_multi_factor_authentication: Optional[CloudAppInfoState] = None
    # The isPasswordPolicy property
    is_password_policy: Optional[CloudAppInfoState] = None
    # The isPasswordPolicyChangePasswordPeriod property
    is_password_policy_change_password_period: Optional[CloudAppInfoState] = None
    # The isPasswordPolicyCharacterCombination property
    is_password_policy_character_combination: Optional[CloudAppInfoState] = None
    # The isPasswordPolicyPasswordHistoryAndReuse property
    is_password_policy_password_history_and_reuse: Optional[CloudAppInfoState] = None
    # The isPasswordPolicyPasswordLengthLimit property
    is_password_policy_password_length_limit: Optional[CloudAppInfoState] = None
    # The isPasswordPolicyPersonalInformationUse property
    is_password_policy_personal_information_use: Optional[CloudAppInfoState] = None
    # The isPenetrationTesting property
    is_penetration_testing: Optional[CloudAppInfoState] = None
    # The isPrivacyShieldCompliant property
    is_privacy_shield_compliant: Optional[CloudAppInfoState] = None
    # The isRememberPassword property
    is_remember_password: Optional[CloudAppInfoState] = None
    # The isRequiresUserAuthentication property
    is_requires_user_authentication: Optional[CloudAppInfoState] = None
    # The isSoc1Compliant property
    is_soc1_compliant: Optional[CloudAppInfoState] = None
    # The isSoc2Compliant property
    is_soc2_compliant: Optional[CloudAppInfoState] = None
    # The isSoc3Compliant property
    is_soc3_compliant: Optional[CloudAppInfoState] = None
    # The isSoxCompliant property
    is_sox_compliant: Optional[CloudAppInfoState] = None
    # The isSp80053Compliant property
    is_sp80053_compliant: Optional[CloudAppInfoState] = None
    # The isSsae16Compliant property
    is_ssae16_compliant: Optional[CloudAppInfoState] = None
    # The isSupportsSaml property
    is_supports_saml: Optional[CloudAppInfoState] = None
    # The isTrustedCertificate property
    is_trusted_certificate: Optional[CloudAppInfoState] = None
    # The isUserAuditTrail property
    is_user_audit_trail: Optional[CloudAppInfoState] = None
    # The isUserCanUploadData property
    is_user_can_upload_data: Optional[CloudAppInfoState] = None
    # The isUserRolesSupport property
    is_user_roles_support: Optional[CloudAppInfoState] = None
    # The isValidCertificateName property
    is_valid_certificate_name: Optional[CloudAppInfoState] = None
    # Indicates the last date of the data breach for the company.
    latest_breach_date_time: Optional[datetime.datetime] = None
    # Indicates the URL that users can use to sign into the app.
    logon_urls: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The pciDssVersion property
    pci_dss_version: Optional[AppInfoPciDssVersion] = None
    # Indicates the app vendor.
    vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DiscoveredCloudAppInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DiscoveredCloudAppInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DiscoveredCloudAppInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .app_info_csa_star_level import AppInfoCsaStarLevel
        from .app_info_data_at_rest_encryption_method import AppInfoDataAtRestEncryptionMethod
        from .app_info_data_retention_policy import AppInfoDataRetentionPolicy
        from .app_info_encryption_protocol import AppInfoEncryptionProtocol
        from .app_info_fed_ramp_level import AppInfoFedRampLevel
        from .app_info_holding import AppInfoHolding
        from .app_info_pci_dss_version import AppInfoPciDssVersion
        from .app_info_uploaded_data_types import AppInfoUploadedDataTypes
        from .cloud_app_info_state import CloudAppInfoState

        from ..entity import Entity
        from .app_info_csa_star_level import AppInfoCsaStarLevel
        from .app_info_data_at_rest_encryption_method import AppInfoDataAtRestEncryptionMethod
        from .app_info_data_retention_policy import AppInfoDataRetentionPolicy
        from .app_info_encryption_protocol import AppInfoEncryptionProtocol
        from .app_info_fed_ramp_level import AppInfoFedRampLevel
        from .app_info_holding import AppInfoHolding
        from .app_info_pci_dss_version import AppInfoPciDssVersion
        from .app_info_uploaded_data_types import AppInfoUploadedDataTypes
        from .cloud_app_info_state import CloudAppInfoState

        fields: dict[str, Callable[[Any], None]] = {
            "csaStarLevel": lambda n : setattr(self, 'csa_star_level', n.get_enum_value(AppInfoCsaStarLevel)),
            "dataAtRestEncryptionMethod": lambda n : setattr(self, 'data_at_rest_encryption_method', n.get_enum_value(AppInfoDataAtRestEncryptionMethod)),
            "dataCenter": lambda n : setattr(self, 'data_center', n.get_str_value()),
            "dataRetentionPolicy": lambda n : setattr(self, 'data_retention_policy', n.get_enum_value(AppInfoDataRetentionPolicy)),
            "dataTypes": lambda n : setattr(self, 'data_types', n.get_collection_of_enum_values(AppInfoUploadedDataTypes)),
            "domainRegistrationDateTime": lambda n : setattr(self, 'domain_registration_date_time', n.get_datetime_value()),
            "encryptionProtocol": lambda n : setattr(self, 'encryption_protocol', n.get_enum_value(AppInfoEncryptionProtocol)),
            "fedRampLevel": lambda n : setattr(self, 'fed_ramp_level', n.get_enum_value(AppInfoFedRampLevel)),
            "founded": lambda n : setattr(self, 'founded', n.get_int_value()),
            "gdprReadinessStatement": lambda n : setattr(self, 'gdpr_readiness_statement', n.get_str_value()),
            "headquarters": lambda n : setattr(self, 'headquarters', n.get_str_value()),
            "holding": lambda n : setattr(self, 'holding', n.get_enum_value(AppInfoHolding)),
            "hostingCompany": lambda n : setattr(self, 'hosting_company', n.get_str_value()),
            "isAdminAuditTrail": lambda n : setattr(self, 'is_admin_audit_trail', n.get_enum_value(CloudAppInfoState)),
            "isCobitCompliant": lambda n : setattr(self, 'is_cobit_compliant', n.get_enum_value(CloudAppInfoState)),
            "isCoppaCompliant": lambda n : setattr(self, 'is_coppa_compliant', n.get_enum_value(CloudAppInfoState)),
            "isDataAuditTrail": lambda n : setattr(self, 'is_data_audit_trail', n.get_enum_value(CloudAppInfoState)),
            "isDataClassification": lambda n : setattr(self, 'is_data_classification', n.get_enum_value(CloudAppInfoState)),
            "isDataOwnership": lambda n : setattr(self, 'is_data_ownership', n.get_enum_value(CloudAppInfoState)),
            "isDisasterRecoveryPlan": lambda n : setattr(self, 'is_disaster_recovery_plan', n.get_enum_value(CloudAppInfoState)),
            "isDmca": lambda n : setattr(self, 'is_dmca', n.get_enum_value(CloudAppInfoState)),
            "isFerpaCompliant": lambda n : setattr(self, 'is_ferpa_compliant', n.get_enum_value(CloudAppInfoState)),
            "isFfiecCompliant": lambda n : setattr(self, 'is_ffiec_compliant', n.get_enum_value(CloudAppInfoState)),
            "isFileSharing": lambda n : setattr(self, 'is_file_sharing', n.get_enum_value(CloudAppInfoState)),
            "isFinraCompliant": lambda n : setattr(self, 'is_finra_compliant', n.get_enum_value(CloudAppInfoState)),
            "isFismaCompliant": lambda n : setattr(self, 'is_fisma_compliant', n.get_enum_value(CloudAppInfoState)),
            "isGaapCompliant": lambda n : setattr(self, 'is_gaap_compliant', n.get_enum_value(CloudAppInfoState)),
            "isGdprDataProtectionImpactAssessment": lambda n : setattr(self, 'is_gdpr_data_protection_impact_assessment', n.get_enum_value(CloudAppInfoState)),
            "isGdprDataProtectionOfficer": lambda n : setattr(self, 'is_gdpr_data_protection_officer', n.get_enum_value(CloudAppInfoState)),
            "isGdprDataProtectionSecureCrossBorderDataTransfer": lambda n : setattr(self, 'is_gdpr_data_protection_secure_cross_border_data_transfer', n.get_enum_value(CloudAppInfoState)),
            "isGdprImpactAssessment": lambda n : setattr(self, 'is_gdpr_impact_assessment', n.get_enum_value(CloudAppInfoState)),
            "isGdprLawfulBasisForProcessing": lambda n : setattr(self, 'is_gdpr_lawful_basis_for_processing', n.get_enum_value(CloudAppInfoState)),
            "isGdprReportDataBreaches": lambda n : setattr(self, 'is_gdpr_report_data_breaches', n.get_enum_value(CloudAppInfoState)),
            "isGdprRightToAccess": lambda n : setattr(self, 'is_gdpr_right_to_access', n.get_enum_value(CloudAppInfoState)),
            "isGdprRightToBeInformed": lambda n : setattr(self, 'is_gdpr_right_to_be_informed', n.get_enum_value(CloudAppInfoState)),
            "isGdprRightToDataPortablility": lambda n : setattr(self, 'is_gdpr_right_to_data_portablility', n.get_enum_value(CloudAppInfoState)),
            "isGdprRightToErasure": lambda n : setattr(self, 'is_gdpr_right_to_erasure', n.get_enum_value(CloudAppInfoState)),
            "isGdprRightToObject": lambda n : setattr(self, 'is_gdpr_right_to_object', n.get_enum_value(CloudAppInfoState)),
            "isGdprRightToRectification": lambda n : setattr(self, 'is_gdpr_right_to_rectification', n.get_enum_value(CloudAppInfoState)),
            "isGdprRightToRestrictionOfProcessing": lambda n : setattr(self, 'is_gdpr_right_to_restriction_of_processing', n.get_enum_value(CloudAppInfoState)),
            "isGdprRightsRelatedToAutomatedDecisionMaking": lambda n : setattr(self, 'is_gdpr_rights_related_to_automated_decision_making', n.get_enum_value(CloudAppInfoState)),
            "isGdprSecureCrossBorderDataControl": lambda n : setattr(self, 'is_gdpr_secure_cross_border_data_control', n.get_enum_value(CloudAppInfoState)),
            "isGlbaCompliant": lambda n : setattr(self, 'is_glba_compliant', n.get_enum_value(CloudAppInfoState)),
            "isHipaaCompliant": lambda n : setattr(self, 'is_hipaa_compliant', n.get_enum_value(CloudAppInfoState)),
            "isHitrustCsfCompliant": lambda n : setattr(self, 'is_hitrust_csf_compliant', n.get_enum_value(CloudAppInfoState)),
            "isHttpSecurityHeadersContentSecurityPolicy": lambda n : setattr(self, 'is_http_security_headers_content_security_policy', n.get_enum_value(CloudAppInfoState)),
            "isHttpSecurityHeadersStrictTransportSecurity": lambda n : setattr(self, 'is_http_security_headers_strict_transport_security', n.get_enum_value(CloudAppInfoState)),
            "isHttpSecurityHeadersXContentTypeOptions": lambda n : setattr(self, 'is_http_security_headers_x_content_type_options', n.get_enum_value(CloudAppInfoState)),
            "isHttpSecurityHeadersXFrameOptions": lambda n : setattr(self, 'is_http_security_headers_x_frame_options', n.get_enum_value(CloudAppInfoState)),
            "isHttpSecurityHeadersXXssProtection": lambda n : setattr(self, 'is_http_security_headers_x_xss_protection', n.get_enum_value(CloudAppInfoState)),
            "isIpAddressRestriction": lambda n : setattr(self, 'is_ip_address_restriction', n.get_enum_value(CloudAppInfoState)),
            "isIsae3402Compliant": lambda n : setattr(self, 'is_isae3402_compliant', n.get_enum_value(CloudAppInfoState)),
            "isIso27001Compliant": lambda n : setattr(self, 'is_iso27001_compliant', n.get_enum_value(CloudAppInfoState)),
            "isIso27017Compliant": lambda n : setattr(self, 'is_iso27017_compliant', n.get_enum_value(CloudAppInfoState)),
            "isIso27018Compliant": lambda n : setattr(self, 'is_iso27018_compliant', n.get_enum_value(CloudAppInfoState)),
            "isItarCompliant": lambda n : setattr(self, 'is_itar_compliant', n.get_enum_value(CloudAppInfoState)),
            "isMultiFactorAuthentication": lambda n : setattr(self, 'is_multi_factor_authentication', n.get_enum_value(CloudAppInfoState)),
            "isPasswordPolicy": lambda n : setattr(self, 'is_password_policy', n.get_enum_value(CloudAppInfoState)),
            "isPasswordPolicyChangePasswordPeriod": lambda n : setattr(self, 'is_password_policy_change_password_period', n.get_enum_value(CloudAppInfoState)),
            "isPasswordPolicyCharacterCombination": lambda n : setattr(self, 'is_password_policy_character_combination', n.get_enum_value(CloudAppInfoState)),
            "isPasswordPolicyPasswordHistoryAndReuse": lambda n : setattr(self, 'is_password_policy_password_history_and_reuse', n.get_enum_value(CloudAppInfoState)),
            "isPasswordPolicyPasswordLengthLimit": lambda n : setattr(self, 'is_password_policy_password_length_limit', n.get_enum_value(CloudAppInfoState)),
            "isPasswordPolicyPersonalInformationUse": lambda n : setattr(self, 'is_password_policy_personal_information_use', n.get_enum_value(CloudAppInfoState)),
            "isPenetrationTesting": lambda n : setattr(self, 'is_penetration_testing', n.get_enum_value(CloudAppInfoState)),
            "isPrivacyShieldCompliant": lambda n : setattr(self, 'is_privacy_shield_compliant', n.get_enum_value(CloudAppInfoState)),
            "isRememberPassword": lambda n : setattr(self, 'is_remember_password', n.get_enum_value(CloudAppInfoState)),
            "isRequiresUserAuthentication": lambda n : setattr(self, 'is_requires_user_authentication', n.get_enum_value(CloudAppInfoState)),
            "isSoc1Compliant": lambda n : setattr(self, 'is_soc1_compliant', n.get_enum_value(CloudAppInfoState)),
            "isSoc2Compliant": lambda n : setattr(self, 'is_soc2_compliant', n.get_enum_value(CloudAppInfoState)),
            "isSoc3Compliant": lambda n : setattr(self, 'is_soc3_compliant', n.get_enum_value(CloudAppInfoState)),
            "isSoxCompliant": lambda n : setattr(self, 'is_sox_compliant', n.get_enum_value(CloudAppInfoState)),
            "isSp80053Compliant": lambda n : setattr(self, 'is_sp80053_compliant', n.get_enum_value(CloudAppInfoState)),
            "isSsae16Compliant": lambda n : setattr(self, 'is_ssae16_compliant', n.get_enum_value(CloudAppInfoState)),
            "isSupportsSaml": lambda n : setattr(self, 'is_supports_saml', n.get_enum_value(CloudAppInfoState)),
            "isTrustedCertificate": lambda n : setattr(self, 'is_trusted_certificate', n.get_enum_value(CloudAppInfoState)),
            "isUserAuditTrail": lambda n : setattr(self, 'is_user_audit_trail', n.get_enum_value(CloudAppInfoState)),
            "isUserCanUploadData": lambda n : setattr(self, 'is_user_can_upload_data', n.get_enum_value(CloudAppInfoState)),
            "isUserRolesSupport": lambda n : setattr(self, 'is_user_roles_support', n.get_enum_value(CloudAppInfoState)),
            "isValidCertificateName": lambda n : setattr(self, 'is_valid_certificate_name', n.get_enum_value(CloudAppInfoState)),
            "latestBreachDateTime": lambda n : setattr(self, 'latest_breach_date_time', n.get_datetime_value()),
            "logonUrls": lambda n : setattr(self, 'logon_urls', n.get_collection_of_primitive_values(str)),
            "pciDssVersion": lambda n : setattr(self, 'pci_dss_version', n.get_enum_value(AppInfoPciDssVersion)),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
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
        writer.write_enum_value("csaStarLevel", self.csa_star_level)
        writer.write_enum_value("dataAtRestEncryptionMethod", self.data_at_rest_encryption_method)
        writer.write_str_value("dataCenter", self.data_center)
        writer.write_enum_value("dataRetentionPolicy", self.data_retention_policy)
        writer.write_collection_of_enum_values("dataTypes", self.data_types)
        writer.write_datetime_value("domainRegistrationDateTime", self.domain_registration_date_time)
        writer.write_enum_value("encryptionProtocol", self.encryption_protocol)
        writer.write_enum_value("fedRampLevel", self.fed_ramp_level)
        writer.write_int_value("founded", self.founded)
        writer.write_str_value("gdprReadinessStatement", self.gdpr_readiness_statement)
        writer.write_str_value("headquarters", self.headquarters)
        writer.write_enum_value("holding", self.holding)
        writer.write_str_value("hostingCompany", self.hosting_company)
        writer.write_enum_value("isAdminAuditTrail", self.is_admin_audit_trail)
        writer.write_enum_value("isCobitCompliant", self.is_cobit_compliant)
        writer.write_enum_value("isCoppaCompliant", self.is_coppa_compliant)
        writer.write_enum_value("isDataAuditTrail", self.is_data_audit_trail)
        writer.write_enum_value("isDataClassification", self.is_data_classification)
        writer.write_enum_value("isDataOwnership", self.is_data_ownership)
        writer.write_enum_value("isDisasterRecoveryPlan", self.is_disaster_recovery_plan)
        writer.write_enum_value("isDmca", self.is_dmca)
        writer.write_enum_value("isFerpaCompliant", self.is_ferpa_compliant)
        writer.write_enum_value("isFfiecCompliant", self.is_ffiec_compliant)
        writer.write_enum_value("isFileSharing", self.is_file_sharing)
        writer.write_enum_value("isFinraCompliant", self.is_finra_compliant)
        writer.write_enum_value("isFismaCompliant", self.is_fisma_compliant)
        writer.write_enum_value("isGaapCompliant", self.is_gaap_compliant)
        writer.write_enum_value("isGdprDataProtectionImpactAssessment", self.is_gdpr_data_protection_impact_assessment)
        writer.write_enum_value("isGdprDataProtectionOfficer", self.is_gdpr_data_protection_officer)
        writer.write_enum_value("isGdprDataProtectionSecureCrossBorderDataTransfer", self.is_gdpr_data_protection_secure_cross_border_data_transfer)
        writer.write_enum_value("isGdprImpactAssessment", self.is_gdpr_impact_assessment)
        writer.write_enum_value("isGdprLawfulBasisForProcessing", self.is_gdpr_lawful_basis_for_processing)
        writer.write_enum_value("isGdprReportDataBreaches", self.is_gdpr_report_data_breaches)
        writer.write_enum_value("isGdprRightToAccess", self.is_gdpr_right_to_access)
        writer.write_enum_value("isGdprRightToBeInformed", self.is_gdpr_right_to_be_informed)
        writer.write_enum_value("isGdprRightToDataPortablility", self.is_gdpr_right_to_data_portablility)
        writer.write_enum_value("isGdprRightToErasure", self.is_gdpr_right_to_erasure)
        writer.write_enum_value("isGdprRightToObject", self.is_gdpr_right_to_object)
        writer.write_enum_value("isGdprRightToRectification", self.is_gdpr_right_to_rectification)
        writer.write_enum_value("isGdprRightToRestrictionOfProcessing", self.is_gdpr_right_to_restriction_of_processing)
        writer.write_enum_value("isGdprRightsRelatedToAutomatedDecisionMaking", self.is_gdpr_rights_related_to_automated_decision_making)
        writer.write_enum_value("isGdprSecureCrossBorderDataControl", self.is_gdpr_secure_cross_border_data_control)
        writer.write_enum_value("isGlbaCompliant", self.is_glba_compliant)
        writer.write_enum_value("isHipaaCompliant", self.is_hipaa_compliant)
        writer.write_enum_value("isHitrustCsfCompliant", self.is_hitrust_csf_compliant)
        writer.write_enum_value("isHttpSecurityHeadersContentSecurityPolicy", self.is_http_security_headers_content_security_policy)
        writer.write_enum_value("isHttpSecurityHeadersStrictTransportSecurity", self.is_http_security_headers_strict_transport_security)
        writer.write_enum_value("isHttpSecurityHeadersXContentTypeOptions", self.is_http_security_headers_x_content_type_options)
        writer.write_enum_value("isHttpSecurityHeadersXFrameOptions", self.is_http_security_headers_x_frame_options)
        writer.write_enum_value("isHttpSecurityHeadersXXssProtection", self.is_http_security_headers_x_xss_protection)
        writer.write_enum_value("isIpAddressRestriction", self.is_ip_address_restriction)
        writer.write_enum_value("isIsae3402Compliant", self.is_isae3402_compliant)
        writer.write_enum_value("isIso27001Compliant", self.is_iso27001_compliant)
        writer.write_enum_value("isIso27017Compliant", self.is_iso27017_compliant)
        writer.write_enum_value("isIso27018Compliant", self.is_iso27018_compliant)
        writer.write_enum_value("isItarCompliant", self.is_itar_compliant)
        writer.write_enum_value("isMultiFactorAuthentication", self.is_multi_factor_authentication)
        writer.write_enum_value("isPasswordPolicy", self.is_password_policy)
        writer.write_enum_value("isPasswordPolicyChangePasswordPeriod", self.is_password_policy_change_password_period)
        writer.write_enum_value("isPasswordPolicyCharacterCombination", self.is_password_policy_character_combination)
        writer.write_enum_value("isPasswordPolicyPasswordHistoryAndReuse", self.is_password_policy_password_history_and_reuse)
        writer.write_enum_value("isPasswordPolicyPasswordLengthLimit", self.is_password_policy_password_length_limit)
        writer.write_enum_value("isPasswordPolicyPersonalInformationUse", self.is_password_policy_personal_information_use)
        writer.write_enum_value("isPenetrationTesting", self.is_penetration_testing)
        writer.write_enum_value("isPrivacyShieldCompliant", self.is_privacy_shield_compliant)
        writer.write_enum_value("isRememberPassword", self.is_remember_password)
        writer.write_enum_value("isRequiresUserAuthentication", self.is_requires_user_authentication)
        writer.write_enum_value("isSoc1Compliant", self.is_soc1_compliant)
        writer.write_enum_value("isSoc2Compliant", self.is_soc2_compliant)
        writer.write_enum_value("isSoc3Compliant", self.is_soc3_compliant)
        writer.write_enum_value("isSoxCompliant", self.is_sox_compliant)
        writer.write_enum_value("isSp80053Compliant", self.is_sp80053_compliant)
        writer.write_enum_value("isSsae16Compliant", self.is_ssae16_compliant)
        writer.write_enum_value("isSupportsSaml", self.is_supports_saml)
        writer.write_enum_value("isTrustedCertificate", self.is_trusted_certificate)
        writer.write_enum_value("isUserAuditTrail", self.is_user_audit_trail)
        writer.write_enum_value("isUserCanUploadData", self.is_user_can_upload_data)
        writer.write_enum_value("isUserRolesSupport", self.is_user_roles_support)
        writer.write_enum_value("isValidCertificateName", self.is_valid_certificate_name)
        writer.write_datetime_value("latestBreachDateTime", self.latest_breach_date_time)
        writer.write_collection_of_primitive_values("logonUrls", self.logon_urls)
        writer.write_enum_value("pciDssVersion", self.pci_dss_version)
        writer.write_str_value("vendor", self.vendor)
    

