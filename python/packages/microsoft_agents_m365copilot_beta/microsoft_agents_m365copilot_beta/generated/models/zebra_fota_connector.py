from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .zebra_fota_connector_state import ZebraFotaConnectorState

from .entity import Entity

@dataclass
class ZebraFotaConnector(Entity, Parsable):
    """
    The Zebra FOTA connector entity that represents the tenant's authorization status for Intune to call Zebra Update Services.
    """
    # Complete account enrollment authorization URL. This corresponds to verification_uri_complete in the Zebra API documentations.
    enrollment_authorization_url: Optional[str] = None
    # Tenant enrollment token from Zebra. The token is used to enroll Zebra devices in the FOTA Service via app config.
    enrollment_token: Optional[str] = None
    # Flag indicating if required Firmware Over-the-Air (FOTA) Apps have been approved.
    fota_apps_approved: Optional[bool] = None
    # Date and time when the account was last synched with Zebra
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents various states for Zebra FOTA connector.
    state: Optional[ZebraFotaConnectorState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ZebraFotaConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ZebraFotaConnector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .zebra_fota_connector_state import ZebraFotaConnectorState

        from .entity import Entity
        from .zebra_fota_connector_state import ZebraFotaConnectorState

        fields: dict[str, Callable[[Any], None]] = {
            "enrollmentAuthorizationUrl": lambda n : setattr(self, 'enrollment_authorization_url', n.get_str_value()),
            "enrollmentToken": lambda n : setattr(self, 'enrollment_token', n.get_str_value()),
            "fotaAppsApproved": lambda n : setattr(self, 'fota_apps_approved', n.get_bool_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ZebraFotaConnectorState)),
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
        writer.write_str_value("enrollmentAuthorizationUrl", self.enrollment_authorization_url)
        writer.write_str_value("enrollmentToken", self.enrollment_token)
        writer.write_bool_value("fotaAppsApproved", self.fota_apps_approved)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_enum_value("state", self.state)
    

