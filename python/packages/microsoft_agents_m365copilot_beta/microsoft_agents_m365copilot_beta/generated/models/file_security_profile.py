from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .file_hash import FileHash
    from .malware_state import MalwareState
    from .security_vendor_information import SecurityVendorInformation
    from .vulnerability_state import VulnerabilityState

from .entity import Entity

@dataclass
class FileSecurityProfile(Entity, Parsable):
    # The activityGroupNames property
    activity_group_names: Optional[list[str]] = None
    # The azureSubscriptionId property
    azure_subscription_id: Optional[str] = None
    # The azureTenantId property
    azure_tenant_id: Optional[str] = None
    # The certificateThumbprint property
    certificate_thumbprint: Optional[str] = None
    # The extensions property
    extensions: Optional[list[str]] = None
    # The fileType property
    file_type: Optional[str] = None
    # The firstSeenDateTime property
    first_seen_date_time: Optional[datetime.datetime] = None
    # The hashes property
    hashes: Optional[list[FileHash]] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime.datetime] = None
    # The malwareStates property
    malware_states: Optional[list[MalwareState]] = None
    # The names property
    names: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskScore property
    risk_score: Optional[str] = None
    # The size property
    size: Optional[int] = None
    # The tags property
    tags: Optional[list[str]] = None
    # The vendorInformation property
    vendor_information: Optional[SecurityVendorInformation] = None
    # The vulnerabilityStates property
    vulnerability_states: Optional[list[VulnerabilityState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileSecurityProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileSecurityProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .file_hash import FileHash
        from .malware_state import MalwareState
        from .security_vendor_information import SecurityVendorInformation
        from .vulnerability_state import VulnerabilityState

        from .entity import Entity
        from .file_hash import FileHash
        from .malware_state import MalwareState
        from .security_vendor_information import SecurityVendorInformation
        from .vulnerability_state import VulnerabilityState

        fields: dict[str, Callable[[Any], None]] = {
            "activityGroupNames": lambda n : setattr(self, 'activity_group_names', n.get_collection_of_primitive_values(str)),
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "certificateThumbprint": lambda n : setattr(self, 'certificate_thumbprint', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_primitive_values(str)),
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "hashes": lambda n : setattr(self, 'hashes', n.get_collection_of_object_values(FileHash)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "malwareStates": lambda n : setattr(self, 'malware_states', n.get_collection_of_object_values(MalwareState)),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_primitive_values(str)),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(SecurityVendorInformation)),
            "vulnerabilityStates": lambda n : setattr(self, 'vulnerability_states', n.get_collection_of_object_values(VulnerabilityState)),
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
        writer.write_collection_of_primitive_values("activityGroupNames", self.activity_group_names)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_str_value("certificateThumbprint", self.certificate_thumbprint)
        writer.write_collection_of_primitive_values("extensions", self.extensions)
        writer.write_str_value("fileType", self.file_type)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_collection_of_object_values("hashes", self.hashes)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("malwareStates", self.malware_states)
        writer.write_collection_of_primitive_values("names", self.names)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_int_value("size", self.size)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("vendorInformation", self.vendor_information)
        writer.write_collection_of_object_values("vulnerabilityStates", self.vulnerability_states)
    

