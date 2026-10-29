from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_a_d_premium_p1_feature_utilizations import AzureADPremiumP1FeatureUtilizations
    from .azure_a_d_premium_p2_feature_utilizations import AzureADPremiumP2FeatureUtilizations
    from .entity import Entity
    from .internet_access_feature_utilizations import InternetAccessFeatureUtilizations
    from .private_access_feature_utilizations import PrivateAccessFeatureUtilizations

from .entity import Entity

@dataclass
class AzureADPremiumLicenseInsight(Entity, Parsable):
    # The number of Microsoft Entra ID P1 licenses entitled to the tenant.
    entitled_p1_license_count: Optional[int] = None
    # The number of Microsoft Entra ID P2 licenses entitled to the tenant.
    entitled_p2_license_count: Optional[int] = None
    # The total number of Microsoft Entra ID premium licenses (P1 + P2) entitled to the tenant.
    entitled_total_license_count: Optional[int] = None
    # The utilization data for Microsoft Entra Internet Access features.
    internet_access_feature_utilizations: Optional[InternetAccessFeatureUtilizations] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The p1FeatureUtilizations property
    p1_feature_utilizations: Optional[AzureADPremiumP1FeatureUtilizations] = None
    # The p2FeatureUtilizations property
    p2_feature_utilizations: Optional[AzureADPremiumP2FeatureUtilizations] = None
    # The utilization data for Microsoft Entra Private Access features.
    private_access_feature_utilizations: Optional[PrivateAccessFeatureUtilizations] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureADPremiumLicenseInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureADPremiumLicenseInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureADPremiumLicenseInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .azure_a_d_premium_p1_feature_utilizations import AzureADPremiumP1FeatureUtilizations
        from .azure_a_d_premium_p2_feature_utilizations import AzureADPremiumP2FeatureUtilizations
        from .entity import Entity
        from .internet_access_feature_utilizations import InternetAccessFeatureUtilizations
        from .private_access_feature_utilizations import PrivateAccessFeatureUtilizations

        from .azure_a_d_premium_p1_feature_utilizations import AzureADPremiumP1FeatureUtilizations
        from .azure_a_d_premium_p2_feature_utilizations import AzureADPremiumP2FeatureUtilizations
        from .entity import Entity
        from .internet_access_feature_utilizations import InternetAccessFeatureUtilizations
        from .private_access_feature_utilizations import PrivateAccessFeatureUtilizations

        fields: dict[str, Callable[[Any], None]] = {
            "entitledP1LicenseCount": lambda n : setattr(self, 'entitled_p1_license_count', n.get_int_value()),
            "entitledP2LicenseCount": lambda n : setattr(self, 'entitled_p2_license_count', n.get_int_value()),
            "entitledTotalLicenseCount": lambda n : setattr(self, 'entitled_total_license_count', n.get_int_value()),
            "internetAccessFeatureUtilizations": lambda n : setattr(self, 'internet_access_feature_utilizations', n.get_object_value(InternetAccessFeatureUtilizations)),
            "p1FeatureUtilizations": lambda n : setattr(self, 'p1_feature_utilizations', n.get_object_value(AzureADPremiumP1FeatureUtilizations)),
            "p2FeatureUtilizations": lambda n : setattr(self, 'p2_feature_utilizations', n.get_object_value(AzureADPremiumP2FeatureUtilizations)),
            "privateAccessFeatureUtilizations": lambda n : setattr(self, 'private_access_feature_utilizations', n.get_object_value(PrivateAccessFeatureUtilizations)),
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
        writer.write_int_value("entitledP1LicenseCount", self.entitled_p1_license_count)
        writer.write_int_value("entitledP2LicenseCount", self.entitled_p2_license_count)
        writer.write_int_value("entitledTotalLicenseCount", self.entitled_total_license_count)
        writer.write_object_value("internetAccessFeatureUtilizations", self.internet_access_feature_utilizations)
        writer.write_object_value("p1FeatureUtilizations", self.p1_feature_utilizations)
        writer.write_object_value("p2FeatureUtilizations", self.p2_feature_utilizations)
        writer.write_object_value("privateAccessFeatureUtilizations", self.private_access_feature_utilizations)
    

