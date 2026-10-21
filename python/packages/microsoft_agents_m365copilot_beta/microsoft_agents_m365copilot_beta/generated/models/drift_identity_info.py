from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entra_drift_identity_info import EntraDriftIdentityInfo
    from .local_drift_identity_info import LocalDriftIdentityInfo

@dataclass
class DriftIdentityInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The display name of the identity.
    display_name: Optional[str] = None
    # The unique identifier for the identity within the drift record.
    identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The principal name of the identity.
    principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriftIdentityInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriftIdentityInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entraDriftIdentityInfo".casefold():
            from .entra_drift_identity_info import EntraDriftIdentityInfo

            return EntraDriftIdentityInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.localDriftIdentityInfo".casefold():
            from .local_drift_identity_info import LocalDriftIdentityInfo

            return LocalDriftIdentityInfo()
        return DriftIdentityInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entra_drift_identity_info import EntraDriftIdentityInfo
        from .local_drift_identity_info import LocalDriftIdentityInfo

        from .entra_drift_identity_info import EntraDriftIdentityInfo
        from .local_drift_identity_info import LocalDriftIdentityInfo

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "principalName": lambda n : setattr(self, 'principal_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("principalName", self.principal_name)
        writer.write_additional_data_value(self.additional_data)
    

