from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SelectionDataStatus(AdditionalDataHolder, Parsable):
    """
    Freshness of each source that contributed to a computed balance or selection.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # When the result was evaluated. Always present.
    evaluated_date_time: Optional[datetime.datetime] = None
    # As-of time of the group membership used.
    group_membership_as_of_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # As-of time of the policy configuration used.
    policy_configuration_as_of_date_time: Optional[datetime.datetime] = None
    # As-of time of the usage data used. Omitted when no usage read was performed.
    usage_as_of_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SelectionDataStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelectionDataStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SelectionDataStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "evaluatedDateTime": lambda n : setattr(self, 'evaluated_date_time', n.get_datetime_value()),
            "groupMembershipAsOfDateTime": lambda n : setattr(self, 'group_membership_as_of_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyConfigurationAsOfDateTime": lambda n : setattr(self, 'policy_configuration_as_of_date_time', n.get_datetime_value()),
            "usageAsOfDateTime": lambda n : setattr(self, 'usage_as_of_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("evaluatedDateTime", self.evaluated_date_time)
        writer.write_datetime_value("groupMembershipAsOfDateTime", self.group_membership_as_of_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("policyConfigurationAsOfDateTime", self.policy_configuration_as_of_date_time)
        writer.write_datetime_value("usageAsOfDateTime", self.usage_as_of_date_time)
        writer.write_additional_data_value(self.additional_data)
    

