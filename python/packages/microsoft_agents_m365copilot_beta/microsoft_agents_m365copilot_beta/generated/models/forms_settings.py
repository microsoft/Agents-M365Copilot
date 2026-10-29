from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FormsSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Controls whether users can add images from Bing to forms.
    is_bing_image_search_enabled: Optional[bool] = None
    # Controls whether users can send a link to a form to an external user.
    is_external_send_form_enabled: Optional[bool] = None
    # Controls whether users can collaborate on a form layout and structure with an external user.
    is_external_share_collaboration_enabled: Optional[bool] = None
    # Controls whether users can share form results with external users.
    is_external_share_result_enabled: Optional[bool] = None
    # Controls whether users can share form templates with external users.
    is_external_share_template_enabled: Optional[bool] = None
    # Controls whether phishing protection is run on forms created by users, blocking the creation of forms if common phishing questions are detected.
    is_in_org_forms_phishing_scan_enabled: Optional[bool] = None
    # Controls whether the names of users who fill out forms are recorded.
    is_record_identity_by_default_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FormsSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FormsSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FormsSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isBingImageSearchEnabled": lambda n : setattr(self, 'is_bing_image_search_enabled', n.get_bool_value()),
            "isExternalSendFormEnabled": lambda n : setattr(self, 'is_external_send_form_enabled', n.get_bool_value()),
            "isExternalShareCollaborationEnabled": lambda n : setattr(self, 'is_external_share_collaboration_enabled', n.get_bool_value()),
            "isExternalShareResultEnabled": lambda n : setattr(self, 'is_external_share_result_enabled', n.get_bool_value()),
            "isExternalShareTemplateEnabled": lambda n : setattr(self, 'is_external_share_template_enabled', n.get_bool_value()),
            "isInOrgFormsPhishingScanEnabled": lambda n : setattr(self, 'is_in_org_forms_phishing_scan_enabled', n.get_bool_value()),
            "isRecordIdentityByDefaultEnabled": lambda n : setattr(self, 'is_record_identity_by_default_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("isBingImageSearchEnabled", self.is_bing_image_search_enabled)
        writer.write_bool_value("isExternalSendFormEnabled", self.is_external_send_form_enabled)
        writer.write_bool_value("isExternalShareCollaborationEnabled", self.is_external_share_collaboration_enabled)
        writer.write_bool_value("isExternalShareResultEnabled", self.is_external_share_result_enabled)
        writer.write_bool_value("isExternalShareTemplateEnabled", self.is_external_share_template_enabled)
        writer.write_bool_value("isInOrgFormsPhishingScanEnabled", self.is_in_org_forms_phishing_scan_enabled)
        writer.write_bool_value("isRecordIdentityByDefaultEnabled", self.is_record_identity_by_default_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

