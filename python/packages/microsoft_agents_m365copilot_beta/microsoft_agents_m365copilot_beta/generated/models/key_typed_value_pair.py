from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_boolean_value_pair import KeyBooleanValuePair
    from .key_integer_value_pair import KeyIntegerValuePair
    from .key_real_value_pair import KeyRealValuePair
    from .key_string_value_pair import KeyStringValuePair

@dataclass
class KeyTypedValuePair(AdditionalDataHolder, Parsable):
    """
    A key-value pair with a string key and a typed value.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The string key of the key-value pair.
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KeyTypedValuePair:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KeyTypedValuePair
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.keyBooleanValuePair".casefold():
            from .key_boolean_value_pair import KeyBooleanValuePair

            return KeyBooleanValuePair()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.keyIntegerValuePair".casefold():
            from .key_integer_value_pair import KeyIntegerValuePair

            return KeyIntegerValuePair()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.keyRealValuePair".casefold():
            from .key_real_value_pair import KeyRealValuePair

            return KeyRealValuePair()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.keyStringValuePair".casefold():
            from .key_string_value_pair import KeyStringValuePair

            return KeyStringValuePair()
        return KeyTypedValuePair()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_boolean_value_pair import KeyBooleanValuePair
        from .key_integer_value_pair import KeyIntegerValuePair
        from .key_real_value_pair import KeyRealValuePair
        from .key_string_value_pair import KeyStringValuePair

        from .key_boolean_value_pair import KeyBooleanValuePair
        from .key_integer_value_pair import KeyIntegerValuePair
        from .key_real_value_pair import KeyRealValuePair
        from .key_string_value_pair import KeyStringValuePair

        fields: dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

