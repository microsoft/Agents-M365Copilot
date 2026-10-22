from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_activity import ApplicationActivity

@dataclass
class CloudApplicationMetadata(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activity property
    activity: Optional[ApplicationActivity] = None
    # The list of categories for the application. Supported values are: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.
    categories: Optional[list[str]] = None
    # The ID of the application in the SaaS application catalog.
    cloud_application_catalog_id: Optional[str] = None
    # The compliance score of the application.
    compliance_score: Optional[int] = None
    # The general score of the application.
    general_score: Optional[int] = None
    # The legal score of the application.
    legal_score: Optional[int] = None
    # The username that was used to log into the application.
    login_user: Optional[str] = None
    # The name of the application, for example, ChatGPT, Salesforce, or Bing.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The risk score of the application.
    risk_score: Optional[int] = None
    # The security score of the application.
    security_score: Optional[int] = None
    # A finer-grained activity classification, for example, chat-interaction or tools/call.
    subactivity: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudApplicationMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudApplicationMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudApplicationMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_activity import ApplicationActivity

        from .application_activity import ApplicationActivity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(ApplicationActivity)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "cloudApplicationCatalogId": lambda n : setattr(self, 'cloud_application_catalog_id', n.get_str_value()),
            "complianceScore": lambda n : setattr(self, 'compliance_score', n.get_int_value()),
            "generalScore": lambda n : setattr(self, 'general_score', n.get_int_value()),
            "legalScore": lambda n : setattr(self, 'legal_score', n.get_int_value()),
            "loginUser": lambda n : setattr(self, 'login_user', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_int_value()),
            "securityScore": lambda n : setattr(self, 'security_score', n.get_int_value()),
            "subactivity": lambda n : setattr(self, 'subactivity', n.get_str_value()),
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
        writer.write_enum_value("activity", self.activity)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("cloudApplicationCatalogId", self.cloud_application_catalog_id)
        writer.write_int_value("complianceScore", self.compliance_score)
        writer.write_int_value("generalScore", self.general_score)
        writer.write_int_value("legalScore", self.legal_score)
        writer.write_str_value("loginUser", self.login_user)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("riskScore", self.risk_score)
        writer.write_int_value("securityScore", self.security_score)
        writer.write_str_value("subactivity", self.subactivity)
        writer.write_additional_data_value(self.additional_data)
    

