from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy import Policy
    from .tls_inspection_policy_settings import TlsInspectionPolicySettings

from .policy import Policy

@dataclass
class TlsInspectionPolicy(Policy, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.tlsInspectionPolicy"
    # The timestamp of when the policy was last modified. Supports $filter (eq, ne, not, ge, le, in) and $orderby. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The settings property
    settings: Optional[TlsInspectionPolicySettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TlsInspectionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TlsInspectionPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TlsInspectionPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy import Policy
        from .tls_inspection_policy_settings import TlsInspectionPolicySettings

        from .policy import Policy
        from .tls_inspection_policy_settings import TlsInspectionPolicySettings

        fields: dict[str, Callable[[Any], None]] = {
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(TlsInspectionPolicySettings)),
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
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("settings", self.settings)
    

