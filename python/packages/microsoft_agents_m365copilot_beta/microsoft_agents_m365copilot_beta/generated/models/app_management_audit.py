from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applied_app_management_policy_restriction import AppliedAppManagementPolicyRestriction
    from .directory_audit import DirectoryAudit

from .directory_audit import DirectoryAudit

@dataclass
class AppManagementAudit(DirectoryAudit, Parsable):
    # The appliedAppManagementPolicyRestrictions property
    applied_app_management_policy_restrictions: Optional[list[AppliedAppManagementPolicyRestriction]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppManagementAudit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppManagementAudit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppManagementAudit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .applied_app_management_policy_restriction import AppliedAppManagementPolicyRestriction
        from .directory_audit import DirectoryAudit

        from .applied_app_management_policy_restriction import AppliedAppManagementPolicyRestriction
        from .directory_audit import DirectoryAudit

        fields: dict[str, Callable[[Any], None]] = {
            "appliedAppManagementPolicyRestrictions": lambda n : setattr(self, 'applied_app_management_policy_restrictions', n.get_collection_of_object_values(AppliedAppManagementPolicyRestriction)),
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
        writer.write_collection_of_object_values("appliedAppManagementPolicyRestrictions", self.applied_app_management_policy_restrictions)
    

