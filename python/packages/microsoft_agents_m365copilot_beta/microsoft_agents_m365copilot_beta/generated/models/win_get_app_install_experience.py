from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .run_as_account_type import RunAsAccountType

@dataclass
class WinGetAppInstallExperience(AdditionalDataHolder, Parsable):
    """
    Represents the install experience settings associated with WinGet apps. This is used to ensure the desired install experiences on the target device are taken into account. Required at creation time.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of execution context the app runs in.
    run_as_account: Optional[RunAsAccountType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WinGetAppInstallExperience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WinGetAppInstallExperience
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WinGetAppInstallExperience()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .run_as_account_type import RunAsAccountType

        from .run_as_account_type import RunAsAccountType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(RunAsAccountType)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_additional_data_value(self.additional_data)
    

