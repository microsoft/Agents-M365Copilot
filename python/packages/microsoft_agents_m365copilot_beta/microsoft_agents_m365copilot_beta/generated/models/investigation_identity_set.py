from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity import Identity
    from .identity_set import IdentitySet

from .identity_set import IdentitySet

@dataclass
class InvestigationIdentitySet(IdentitySet, Parsable):
    """
    Open investigation provenance extending shared user, application, and device identities with the recorded agent principal. This computed parent provenance grants no execution credentials or cross-tenant authorization.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.investigationIdentitySet"
    # The initiating agent principal, when recorded by the service.
    agent: Optional[Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvestigationIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvestigationIdentitySet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvestigationIdentitySet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity import Identity
        from .identity_set import IdentitySet

        from .identity import Identity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "agent": lambda n : setattr(self, 'agent', n.get_object_value(Identity)),
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
    

