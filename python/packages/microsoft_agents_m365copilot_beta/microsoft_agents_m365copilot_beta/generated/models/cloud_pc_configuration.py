from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType

@dataclass
class CloudPcConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The display name of the image. Read-only.
    image_display_name: Optional[str] = None
    # The unique identifier of the operating system image used for provisioning new Cloud PCs. The format for a gallery type image is: {publisherNameofferNameskuName}.
    image_id: Optional[str] = None
    # The imageType property
    image_type: Optional[CloudPcProvisioningPolicyImageType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operating system locale for the Cloud PC.
    os_locale: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType

        from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType

        fields: dict[str, Callable[[Any], None]] = {
            "imageDisplayName": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "imageId": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "imageType": lambda n : setattr(self, 'image_type', n.get_enum_value(CloudPcProvisioningPolicyImageType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osLocale": lambda n : setattr(self, 'os_locale', n.get_str_value()),
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
        writer.write_str_value("imageDisplayName", self.image_display_name)
        writer.write_str_value("imageId", self.image_id)
        writer.write_enum_value("imageType", self.image_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osLocale", self.os_locale)
        writer.write_additional_data_value(self.additional_data)
    

