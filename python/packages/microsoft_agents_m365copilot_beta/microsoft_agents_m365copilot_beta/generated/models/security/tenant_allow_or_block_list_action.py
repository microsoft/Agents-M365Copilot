from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tenant_allow_block_list_action import TenantAllowBlockListAction
    from .tenant_allow_block_list_entry_result import TenantAllowBlockListEntryResult

@dataclass
class TenantAllowOrBlockListAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies whether the tenant allow-or-block list is an allow or block. The possible values are: allow, block, and unkownFutureValue.
    action: Optional[TenantAllowBlockListAction] = None
    # Specifies when the tenant allow-block-list expires in date time.
    expiration_date_time: Optional[datetime.datetime] = None
    # Specifies the note added to the tenant allow-or-block list entry in the format of string.
    note: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the result of the submission that lead to the tenant allow-block-list entry creation.
    results: Optional[list[TenantAllowBlockListEntryResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantAllowOrBlockListAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantAllowOrBlockListAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantAllowOrBlockListAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tenant_allow_block_list_action import TenantAllowBlockListAction
        from .tenant_allow_block_list_entry_result import TenantAllowBlockListEntryResult

        from .tenant_allow_block_list_action import TenantAllowBlockListAction
        from .tenant_allow_block_list_entry_result import TenantAllowBlockListEntryResult

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(TenantAllowBlockListAction)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(TenantAllowBlockListEntryResult)),
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
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("note", self.note)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_additional_data_value(self.additional_data)
    

