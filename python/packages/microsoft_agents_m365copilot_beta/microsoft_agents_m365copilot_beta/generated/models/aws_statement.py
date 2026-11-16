from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_condition import AwsCondition
    from .aws_statement_effect import AwsStatementEffect

@dataclass
class AwsStatement(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The AWS actions.
    actions: Optional[list[str]] = None
    # The AWS conditions associated with the statement.
    condition: Optional[AwsCondition] = None
    # The effect property
    effect: Optional[AwsStatementEffect] = None
    # AWS Not Actions
    not_actions: Optional[list[str]] = None
    # AWS Not Resources
    not_resources: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The AWS resources associated with the statement.
    resources: Optional[list[str]] = None
    # The ID of the AWS statement.
    statement_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsStatement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsStatement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AwsStatement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aws_condition import AwsCondition
        from .aws_statement_effect import AwsStatementEffect

        from .aws_condition import AwsCondition
        from .aws_statement_effect import AwsStatementEffect

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_primitive_values(str)),
            "condition": lambda n : setattr(self, 'condition', n.get_object_value(AwsCondition)),
            "effect": lambda n : setattr(self, 'effect', n.get_enum_value(AwsStatementEffect)),
            "notActions": lambda n : setattr(self, 'not_actions', n.get_collection_of_primitive_values(str)),
            "notResources": lambda n : setattr(self, 'not_resources', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_primitive_values(str)),
            "statementId": lambda n : setattr(self, 'statement_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("actions", self.actions)
        writer.write_object_value("condition", self.condition)
        writer.write_enum_value("effect", self.effect)
        writer.write_collection_of_primitive_values("notActions", self.not_actions)
        writer.write_collection_of_primitive_values("notResources", self.not_resources)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("resources", self.resources)
        writer.write_str_value("statementId", self.statement_id)
        writer.write_additional_data_value(self.additional_data)
    

