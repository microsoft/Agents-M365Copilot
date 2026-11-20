from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OnPremisesCurrentExportData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The name of the onPremises client machine that ran the last export.
    client_machine_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The count of pending adds from on-premises directory.
    pending_objects_addition: Optional[int] = None
    # The count of pending deletes from on-premises directory.
    pending_objects_deletion: Optional[int] = None
    # The count of pending updates from on-premises directory.
    pending_objects_update: Optional[int] = None
    # The name of the dirsync service account that is configured to connect to the directory.
    service_account: Optional[str] = None
    # The count of updated links during the current directory sync export run.
    successful_links_provisioning_count: Optional[int] = None
    # The count of objects that were successfully provisioned during the current directory sync export run.
    successful_objects_provisioning_count: Optional[int] = None
    # The total number of objects in the AAD Connector Space.
    total_connector_space_objects: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesCurrentExportData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesCurrentExportData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesCurrentExportData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "clientMachineName": lambda n : setattr(self, 'client_machine_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pendingObjectsAddition": lambda n : setattr(self, 'pending_objects_addition', n.get_int_value()),
            "pendingObjectsDeletion": lambda n : setattr(self, 'pending_objects_deletion', n.get_int_value()),
            "pendingObjectsUpdate": lambda n : setattr(self, 'pending_objects_update', n.get_int_value()),
            "serviceAccount": lambda n : setattr(self, 'service_account', n.get_str_value()),
            "successfulLinksProvisioningCount": lambda n : setattr(self, 'successful_links_provisioning_count', n.get_int_value()),
            "successfulObjectsProvisioningCount": lambda n : setattr(self, 'successful_objects_provisioning_count', n.get_int_value()),
            "totalConnectorSpaceObjects": lambda n : setattr(self, 'total_connector_space_objects', n.get_int_value()),
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
        writer.write_str_value("clientMachineName", self.client_machine_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("pendingObjectsAddition", self.pending_objects_addition)
        writer.write_int_value("pendingObjectsDeletion", self.pending_objects_deletion)
        writer.write_int_value("pendingObjectsUpdate", self.pending_objects_update)
        writer.write_str_value("serviceAccount", self.service_account)
        writer.write_int_value("successfulLinksProvisioningCount", self.successful_links_provisioning_count)
        writer.write_int_value("successfulObjectsProvisioningCount", self.successful_objects_provisioning_count)
        writer.write_int_value("totalConnectorSpaceObjects", self.total_connector_space_objects)
        writer.write_additional_data_value(self.additional_data)
    

