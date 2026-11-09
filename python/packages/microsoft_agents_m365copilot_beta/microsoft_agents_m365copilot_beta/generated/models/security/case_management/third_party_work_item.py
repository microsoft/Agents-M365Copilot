from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .third_party_work_item_metadata import ThirdPartyWorkItemMetadata
    from .third_party_work_item_provider import ThirdPartyWorkItemProvider
    from .third_party_work_item_type import ThirdPartyWorkItemType

@dataclass
class ThirdPartyWorkItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The identifier property
    identifier: Optional[str] = None
    # The instance property
    instance: Optional[str] = None
    # The lastSyncedOnDateTime property
    last_synced_on_date_time: Optional[datetime.datetime] = None
    # The metadata property
    metadata: Optional[ThirdPartyWorkItemMetadata] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The provider property
    provider: Optional[ThirdPartyWorkItemProvider] = None
    # The syncedBy property
    synced_by: Optional[str] = None
    # The workItemType property
    work_item_type: Optional[ThirdPartyWorkItemType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThirdPartyWorkItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThirdPartyWorkItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThirdPartyWorkItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .third_party_work_item_metadata import ThirdPartyWorkItemMetadata
        from .third_party_work_item_provider import ThirdPartyWorkItemProvider
        from .third_party_work_item_type import ThirdPartyWorkItemType

        from .third_party_work_item_metadata import ThirdPartyWorkItemMetadata
        from .third_party_work_item_provider import ThirdPartyWorkItemProvider
        from .third_party_work_item_type import ThirdPartyWorkItemType

        fields: dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "instance": lambda n : setattr(self, 'instance', n.get_str_value()),
            "lastSyncedOnDateTime": lambda n : setattr(self, 'last_synced_on_date_time', n.get_datetime_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(ThirdPartyWorkItemMetadata)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_enum_value(ThirdPartyWorkItemProvider)),
            "syncedBy": lambda n : setattr(self, 'synced_by', n.get_str_value()),
            "workItemType": lambda n : setattr(self, 'work_item_type', n.get_enum_value(ThirdPartyWorkItemType)),
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
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("instance", self.instance)
        writer.write_datetime_value("lastSyncedOnDateTime", self.last_synced_on_date_time)
        writer.write_object_value("metadata", self.metadata)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("provider", self.provider)
        writer.write_str_value("syncedBy", self.synced_by)
        writer.write_enum_value("workItemType", self.work_item_type)
        writer.write_additional_data_value(self.additional_data)
    

