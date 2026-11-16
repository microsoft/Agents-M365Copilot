from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .partner_security_alert import PartnerSecurityAlert
    from .partner_security_score import PartnerSecurityScore

from ...entity import Entity

@dataclass
class PartnerSecurity(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The security alerts or a vulnerability of a Cloud Solution Provider (CSP) partner's customer that the partner must be made aware of for further action.
    security_alerts: Optional[list[PartnerSecurityAlert]] = None
    # The security score calculated for the CSP partner and their customers.
    security_score: Optional[PartnerSecurityScore] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PartnerSecurity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PartnerSecurity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PartnerSecurity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .partner_security_alert import PartnerSecurityAlert
        from .partner_security_score import PartnerSecurityScore

        from ...entity import Entity
        from .partner_security_alert import PartnerSecurityAlert
        from .partner_security_score import PartnerSecurityScore

        fields: dict[str, Callable[[Any], None]] = {
            "securityAlerts": lambda n : setattr(self, 'security_alerts', n.get_collection_of_object_values(PartnerSecurityAlert)),
            "securityScore": lambda n : setattr(self, 'security_score', n.get_object_value(PartnerSecurityScore)),
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
        writer.write_collection_of_object_values("securityAlerts", self.security_alerts)
        writer.write_object_value("securityScore", self.security_score)
    

