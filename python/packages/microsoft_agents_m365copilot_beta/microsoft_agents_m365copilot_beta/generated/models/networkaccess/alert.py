from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_action import AlertAction
    from .alert_severity import AlertSeverity
    from .alert_type import AlertType
    from .extended_properties import ExtendedProperties
    from .filtering_policy import FilteringPolicy
    from .intent_category import IntentCategory
    from .related_resource import RelatedResource

from ..entity import Entity

@dataclass
class Alert(Entity, Parsable):
    # List of possible action items to take based on the alert (if applicable).
    actions: Optional[list[AlertAction]] = None
    # The alertType property
    alert_type: Optional[AlertType] = None
    # Categories associated with the alert.
    categories: Optional[list[IntentCategory]] = None
    # Component name related to the alert.
    component_name: Optional[str] = None
    # The time the alert was created in the system. Required.
    creation_date_time: Optional[datetime.datetime] = None
    # Text description explaining the alert.
    description: Optional[str] = None
    # Alert detection technology.
    detection_technology: Optional[str] = None
    # The display name of the alert. Required.
    display_name: Optional[str] = None
    # Extended properties for the alert.
    extended_properties: Optional[ExtendedProperties] = None
    # The time of the first activity related to the alert.
    first_activity_date_time: Optional[datetime.datetime] = None
    # Indicates if the alert is a preview.
    is_preview: Optional[bool] = None
    # The time of the last activity related to the alert.
    last_activity_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The filtering policy associated with the alert. This relationship allows you to retrieve or manage the filtering policy that triggered or is related to the alert instance.
    policy: Optional[FilteringPolicy] = None
    # The name of the product that raised the alert.
    product_name: Optional[str] = None
    # List of related resources to the alert (if applicable).
    related_resources: Optional[list[RelatedResource]] = None
    # The severity property
    severity: Optional[AlertSeverity] = None
    # Sub-techniques associated with the alert.
    sub_techniques: Optional[list[str]] = None
    # Techniques associated with the alert.
    techniques: Optional[list[str]] = None
    # The name of the vendor that raised the alert.
    vendor_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Alert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Alert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Alert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_action import AlertAction
        from .alert_severity import AlertSeverity
        from .alert_type import AlertType
        from .extended_properties import ExtendedProperties
        from .filtering_policy import FilteringPolicy
        from .intent_category import IntentCategory
        from .related_resource import RelatedResource

        from ..entity import Entity
        from .alert_action import AlertAction
        from .alert_severity import AlertSeverity
        from .alert_type import AlertType
        from .extended_properties import ExtendedProperties
        from .filtering_policy import FilteringPolicy
        from .intent_category import IntentCategory
        from .related_resource import RelatedResource

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AlertAction)),
            "alertType": lambda n : setattr(self, 'alert_type', n.get_enum_value(AlertType)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_enum_values(IntentCategory)),
            "componentName": lambda n : setattr(self, 'component_name', n.get_str_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectionTechnology": lambda n : setattr(self, 'detection_technology', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extendedProperties": lambda n : setattr(self, 'extended_properties', n.get_object_value(ExtendedProperties)),
            "firstActivityDateTime": lambda n : setattr(self, 'first_activity_date_time', n.get_datetime_value()),
            "isPreview": lambda n : setattr(self, 'is_preview', n.get_bool_value()),
            "lastActivityDateTime": lambda n : setattr(self, 'last_activity_date_time', n.get_datetime_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(FilteringPolicy)),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "relatedResources": lambda n : setattr(self, 'related_resources', n.get_collection_of_object_values(RelatedResource)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AlertSeverity)),
            "subTechniques": lambda n : setattr(self, 'sub_techniques', n.get_collection_of_primitive_values(str)),
            "techniques": lambda n : setattr(self, 'techniques', n.get_collection_of_primitive_values(str)),
            "vendorName": lambda n : setattr(self, 'vendor_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_enum_value("alertType", self.alert_type)
        writer.write_collection_of_enum_values("categories", self.categories)
        writer.write_str_value("componentName", self.component_name)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("detectionTechnology", self.detection_technology)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("extendedProperties", self.extended_properties)
        writer.write_datetime_value("firstActivityDateTime", self.first_activity_date_time)
        writer.write_bool_value("isPreview", self.is_preview)
        writer.write_datetime_value("lastActivityDateTime", self.last_activity_date_time)
        writer.write_object_value("policy", self.policy)
        writer.write_str_value("productName", self.product_name)
        writer.write_collection_of_object_values("relatedResources", self.related_resources)
        writer.write_enum_value("severity", self.severity)
        writer.write_collection_of_primitive_values("subTechniques", self.sub_techniques)
        writer.write_collection_of_primitive_values("techniques", self.techniques)
        writer.write_str_value("vendorName", self.vendor_name)
    

