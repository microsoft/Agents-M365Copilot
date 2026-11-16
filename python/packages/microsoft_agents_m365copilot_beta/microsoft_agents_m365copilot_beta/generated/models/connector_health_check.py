from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connector_health_check_metric_name import ConnectorHealthCheckMetricName
    from .ndes_connector_health_status import NdesConnectorHealthStatus

@dataclass
class ConnectorHealthCheck(AdditionalDataHolder, Parsable):
    """
    Represents an individual health check result for an NDES connector, containing the metric name and its current status.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The name of the health check metric being evaluated for an NDES connector.
    metric_name: Optional[ConnectorHealthCheckMetricName] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The health status of an NDES connector or individual health check metric.
    status: Optional[NdesConnectorHealthStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectorHealthCheck:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectorHealthCheck
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectorHealthCheck()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connector_health_check_metric_name import ConnectorHealthCheckMetricName
        from .ndes_connector_health_status import NdesConnectorHealthStatus

        from .connector_health_check_metric_name import ConnectorHealthCheckMetricName
        from .ndes_connector_health_status import NdesConnectorHealthStatus

        fields: dict[str, Callable[[Any], None]] = {
            "metricName": lambda n : setattr(self, 'metric_name', n.get_enum_value(ConnectorHealthCheckMetricName)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(NdesConnectorHealthStatus)),
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
        writer.write_enum_value("metricName", self.metric_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

