from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .related_destination import RelatedDestination
    from .related_device import RelatedDevice
    from .related_file import RelatedFile
    from .related_file_hash import RelatedFileHash
    from .related_malware import RelatedMalware
    from .related_remote_network import RelatedRemoteNetwork
    from .related_tenant import RelatedTenant
    from .related_threat_intelligence import RelatedThreatIntelligence
    from .related_token import RelatedToken
    from .related_transaction import RelatedTransaction
    from .related_url import RelatedUrl
    from .related_user import RelatedUser
    from .related_web_category import RelatedWebCategory

@dataclass
class RelatedResource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelatedResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelatedResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedDestination".casefold():
            from .related_destination import RelatedDestination

            return RelatedDestination()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedDevice".casefold():
            from .related_device import RelatedDevice

            return RelatedDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedFile".casefold():
            from .related_file import RelatedFile

            return RelatedFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedFileHash".casefold():
            from .related_file_hash import RelatedFileHash

            return RelatedFileHash()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedMalware".casefold():
            from .related_malware import RelatedMalware

            return RelatedMalware()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedRemoteNetwork".casefold():
            from .related_remote_network import RelatedRemoteNetwork

            return RelatedRemoteNetwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedTenant".casefold():
            from .related_tenant import RelatedTenant

            return RelatedTenant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedThreatIntelligence".casefold():
            from .related_threat_intelligence import RelatedThreatIntelligence

            return RelatedThreatIntelligence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedToken".casefold():
            from .related_token import RelatedToken

            return RelatedToken()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedTransaction".casefold():
            from .related_transaction import RelatedTransaction

            return RelatedTransaction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedUrl".casefold():
            from .related_url import RelatedUrl

            return RelatedUrl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedUser".casefold():
            from .related_user import RelatedUser

            return RelatedUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedWebCategory".casefold():
            from .related_web_category import RelatedWebCategory

            return RelatedWebCategory()
        return RelatedResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .related_destination import RelatedDestination
        from .related_device import RelatedDevice
        from .related_file import RelatedFile
        from .related_file_hash import RelatedFileHash
        from .related_malware import RelatedMalware
        from .related_remote_network import RelatedRemoteNetwork
        from .related_tenant import RelatedTenant
        from .related_threat_intelligence import RelatedThreatIntelligence
        from .related_token import RelatedToken
        from .related_transaction import RelatedTransaction
        from .related_url import RelatedUrl
        from .related_user import RelatedUser
        from .related_web_category import RelatedWebCategory

        from .related_destination import RelatedDestination
        from .related_device import RelatedDevice
        from .related_file import RelatedFile
        from .related_file_hash import RelatedFileHash
        from .related_malware import RelatedMalware
        from .related_remote_network import RelatedRemoteNetwork
        from .related_tenant import RelatedTenant
        from .related_threat_intelligence import RelatedThreatIntelligence
        from .related_token import RelatedToken
        from .related_transaction import RelatedTransaction
        from .related_url import RelatedUrl
        from .related_user import RelatedUser
        from .related_web_category import RelatedWebCategory

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

