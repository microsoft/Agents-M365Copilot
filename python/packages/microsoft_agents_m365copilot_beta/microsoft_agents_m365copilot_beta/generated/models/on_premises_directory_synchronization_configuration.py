from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .on_premises_accidental_deletion_prevention import OnPremisesAccidentalDeletionPrevention
    from .on_premises_current_export_data import OnPremisesCurrentExportData
    from .on_premises_writeback_configuration import OnPremisesWritebackConfiguration

@dataclass
class OnPremisesDirectorySynchronizationConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains the accidental deletion prevention configuration for a tenant.
    accidental_deletion_prevention: Optional[OnPremisesAccidentalDeletionPrevention] = None
    # The anchor attribute allows customers to customize the property used to create source anchors for synchronization enabled objects.
    anchor_attribute: Optional[str] = None
    # The identifier of the on-premises directory synchronization client application that is configured for the tenant.
    application_id: Optional[str] = None
    # Data for the current export run.
    current_export_data: Optional[OnPremisesCurrentExportData] = None
    # Interval of time that the customer requested the sync client waits between sync cycles.
    customer_requested_synchronization_interval: Optional[datetime.timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the version of the on-premises directory synchronization application.
    synchronization_client_version: Optional[str] = None
    # Interval of time the sync client should honor between sync cycles
    synchronization_interval: Optional[datetime.timedelta] = None
    # Configuration to control how cloud created or owned objects are synchronized back to the on-premises directory.
    writeback_configuration: Optional[OnPremisesWritebackConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesDirectorySynchronizationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronizationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesDirectorySynchronizationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .on_premises_accidental_deletion_prevention import OnPremisesAccidentalDeletionPrevention
        from .on_premises_current_export_data import OnPremisesCurrentExportData
        from .on_premises_writeback_configuration import OnPremisesWritebackConfiguration

        from .on_premises_accidental_deletion_prevention import OnPremisesAccidentalDeletionPrevention
        from .on_premises_current_export_data import OnPremisesCurrentExportData
        from .on_premises_writeback_configuration import OnPremisesWritebackConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "accidentalDeletionPrevention": lambda n : setattr(self, 'accidental_deletion_prevention', n.get_object_value(OnPremisesAccidentalDeletionPrevention)),
            "anchorAttribute": lambda n : setattr(self, 'anchor_attribute', n.get_str_value()),
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "currentExportData": lambda n : setattr(self, 'current_export_data', n.get_object_value(OnPremisesCurrentExportData)),
            "customerRequestedSynchronizationInterval": lambda n : setattr(self, 'customer_requested_synchronization_interval', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "synchronizationClientVersion": lambda n : setattr(self, 'synchronization_client_version', n.get_str_value()),
            "synchronizationInterval": lambda n : setattr(self, 'synchronization_interval', n.get_timedelta_value()),
            "writebackConfiguration": lambda n : setattr(self, 'writeback_configuration', n.get_object_value(OnPremisesWritebackConfiguration)),
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
        writer.write_object_value("accidentalDeletionPrevention", self.accidental_deletion_prevention)
        writer.write_str_value("anchorAttribute", self.anchor_attribute)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_object_value("currentExportData", self.current_export_data)
        writer.write_timedelta_value("customerRequestedSynchronizationInterval", self.customer_requested_synchronization_interval)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("synchronizationClientVersion", self.synchronization_client_version)
        writer.write_timedelta_value("synchronizationInterval", self.synchronization_interval)
        writer.write_object_value("writebackConfiguration", self.writeback_configuration)
        writer.write_additional_data_value(self.additional_data)
    

