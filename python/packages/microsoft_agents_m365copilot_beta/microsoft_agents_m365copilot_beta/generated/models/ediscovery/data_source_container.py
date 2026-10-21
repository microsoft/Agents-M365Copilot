from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .case_index_operation import CaseIndexOperation
    from .custodian import Custodian
    from .data_source_container_status import DataSourceContainerStatus
    from .data_source_hold_status import DataSourceHoldStatus
    from .noncustodial_data_source import NoncustodialDataSource

from ..entity import Entity

@dataclass
class DataSourceContainer(Entity, Parsable):
    # Created date and time of the dataSourceContainer entity.
    created_date_time: Optional[datetime.datetime] = None
    # Display name of the dataSourceContainer entity.
    display_name: Optional[str] = None
    # The holdStatus property
    hold_status: Optional[DataSourceHoldStatus] = None
    # The lastIndexOperation property
    last_index_operation: Optional[CaseIndexOperation] = None
    # Last modified date and time of the dataSourceContainer.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date and time that the dataSourceContainer was released from the case.
    released_date_time: Optional[datetime.datetime] = None
    # Latest status of the dataSourceContainer. The possible values are: Active, Released.
    status: Optional[DataSourceContainerStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataSourceContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataSourceContainer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.custodian".casefold():
            from .custodian import Custodian

            return Custodian()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ediscovery.noncustodialDataSource".casefold():
            from .noncustodial_data_source import NoncustodialDataSource

            return NoncustodialDataSource()
        return DataSourceContainer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .case_index_operation import CaseIndexOperation
        from .custodian import Custodian
        from .data_source_container_status import DataSourceContainerStatus
        from .data_source_hold_status import DataSourceHoldStatus
        from .noncustodial_data_source import NoncustodialDataSource

        from ..entity import Entity
        from .case_index_operation import CaseIndexOperation
        from .custodian import Custodian
        from .data_source_container_status import DataSourceContainerStatus
        from .data_source_hold_status import DataSourceHoldStatus
        from .noncustodial_data_source import NoncustodialDataSource

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "holdStatus": lambda n : setattr(self, 'hold_status', n.get_enum_value(DataSourceHoldStatus)),
            "lastIndexOperation": lambda n : setattr(self, 'last_index_operation', n.get_object_value(CaseIndexOperation)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "releasedDateTime": lambda n : setattr(self, 'released_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DataSourceContainerStatus)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("holdStatus", self.hold_status)
        writer.write_object_value("lastIndexOperation", self.last_index_operation)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("releasedDateTime", self.released_date_time)
        writer.write_enum_value("status", self.status)
    

