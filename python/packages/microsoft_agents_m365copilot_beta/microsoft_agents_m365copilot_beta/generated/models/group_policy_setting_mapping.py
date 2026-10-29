from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .group_policy_setting_scope import GroupPolicySettingScope
    from .group_policy_setting_type import GroupPolicySettingType
    from .mdm_supported_state import MdmSupportedState

from .entity import Entity

@dataclass
class GroupPolicySettingMapping(Entity, Parsable):
    """
    The Group Policy setting to MDM/Intune mapping.
    """
    # Admx Group Policy Id
    admx_setting_definition_id: Optional[str] = None
    # List of Child Ids of the group policy setting.
    child_id_list: Optional[list[str]] = None
    # The Intune Setting Definition Id
    intune_setting_definition_id: Optional[str] = None
    # The list of Intune Setting URIs this group policy setting maps to
    intune_setting_uri_list: Optional[list[str]] = None
    # Indicates if the setting is supported by Intune or not
    is_mdm_supported: Optional[bool] = None
    # The CSP name this group policy setting maps to.
    mdm_csp_name: Optional[str] = None
    # The minimum OS version this mdm setting supports.
    mdm_minimum_o_s_version: Optional[int] = None
    # The MDM CSP URI this group policy setting maps to.
    mdm_setting_uri: Optional[str] = None
    # Mdm Support Status of the setting.
    mdm_supported_state: Optional[MdmSupportedState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Parent Id of the group policy setting.
    parent_id: Optional[str] = None
    # The category the group policy setting is in.
    setting_category: Optional[str] = None
    # The display name of this group policy setting.
    setting_display_name: Optional[str] = None
    # The display value of this group policy setting.
    setting_display_value: Optional[str] = None
    # The display value type of this group policy setting.
    setting_display_value_type: Optional[str] = None
    # The name of this group policy setting.
    setting_name: Optional[str] = None
    # Scope of the group policy setting.
    setting_scope: Optional[GroupPolicySettingScope] = None
    # Setting type of the group policy.
    setting_type: Optional[GroupPolicySettingType] = None
    # The value of this group policy setting.
    setting_value: Optional[str] = None
    # The display units of this group policy setting value
    setting_value_display_units: Optional[str] = None
    # The value type of this group policy setting.
    setting_value_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicySettingMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicySettingMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicySettingMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group_policy_setting_scope import GroupPolicySettingScope
        from .group_policy_setting_type import GroupPolicySettingType
        from .mdm_supported_state import MdmSupportedState

        from .entity import Entity
        from .group_policy_setting_scope import GroupPolicySettingScope
        from .group_policy_setting_type import GroupPolicySettingType
        from .mdm_supported_state import MdmSupportedState

        fields: dict[str, Callable[[Any], None]] = {
            "admxSettingDefinitionId": lambda n : setattr(self, 'admx_setting_definition_id', n.get_str_value()),
            "childIdList": lambda n : setattr(self, 'child_id_list', n.get_collection_of_primitive_values(str)),
            "intuneSettingDefinitionId": lambda n : setattr(self, 'intune_setting_definition_id', n.get_str_value()),
            "intuneSettingUriList": lambda n : setattr(self, 'intune_setting_uri_list', n.get_collection_of_primitive_values(str)),
            "isMdmSupported": lambda n : setattr(self, 'is_mdm_supported', n.get_bool_value()),
            "mdmCspName": lambda n : setattr(self, 'mdm_csp_name', n.get_str_value()),
            "mdmMinimumOSVersion": lambda n : setattr(self, 'mdm_minimum_o_s_version', n.get_int_value()),
            "mdmSettingUri": lambda n : setattr(self, 'mdm_setting_uri', n.get_str_value()),
            "mdmSupportedState": lambda n : setattr(self, 'mdm_supported_state', n.get_enum_value(MdmSupportedState)),
            "parentId": lambda n : setattr(self, 'parent_id', n.get_str_value()),
            "settingCategory": lambda n : setattr(self, 'setting_category', n.get_str_value()),
            "settingDisplayName": lambda n : setattr(self, 'setting_display_name', n.get_str_value()),
            "settingDisplayValue": lambda n : setattr(self, 'setting_display_value', n.get_str_value()),
            "settingDisplayValueType": lambda n : setattr(self, 'setting_display_value_type', n.get_str_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "settingScope": lambda n : setattr(self, 'setting_scope', n.get_enum_value(GroupPolicySettingScope)),
            "settingType": lambda n : setattr(self, 'setting_type', n.get_enum_value(GroupPolicySettingType)),
            "settingValue": lambda n : setattr(self, 'setting_value', n.get_str_value()),
            "settingValueDisplayUnits": lambda n : setattr(self, 'setting_value_display_units', n.get_str_value()),
            "settingValueType": lambda n : setattr(self, 'setting_value_type', n.get_str_value()),
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
        writer.write_str_value("admxSettingDefinitionId", self.admx_setting_definition_id)
        writer.write_collection_of_primitive_values("childIdList", self.child_id_list)
        writer.write_str_value("intuneSettingDefinitionId", self.intune_setting_definition_id)
        writer.write_collection_of_primitive_values("intuneSettingUriList", self.intune_setting_uri_list)
        writer.write_bool_value("isMdmSupported", self.is_mdm_supported)
        writer.write_str_value("mdmCspName", self.mdm_csp_name)
        writer.write_int_value("mdmMinimumOSVersion", self.mdm_minimum_o_s_version)
        writer.write_str_value("mdmSettingUri", self.mdm_setting_uri)
        writer.write_enum_value("mdmSupportedState", self.mdm_supported_state)
        writer.write_str_value("parentId", self.parent_id)
        writer.write_str_value("settingCategory", self.setting_category)
        writer.write_str_value("settingDisplayName", self.setting_display_name)
        writer.write_str_value("settingDisplayValue", self.setting_display_value)
        writer.write_str_value("settingDisplayValueType", self.setting_display_value_type)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_enum_value("settingScope", self.setting_scope)
        writer.write_enum_value("settingType", self.setting_type)
        writer.write_str_value("settingValue", self.setting_value)
        writer.write_str_value("settingValueDisplayUnits", self.setting_value_display_units)
        writer.write_str_value("settingValueType", self.setting_value_type)
    

