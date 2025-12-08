from dataclasses import dataclass
from Options import Range, PerGameCommonOptions


class RequiredWeaponCategories(Range):
    """How many different weapon categories must be available for a monster to be considered in logic"""
    display_name = "Required Weapon Categories"
    range_start = 1
    range_end = 13
    default = 2

@dataclass
class MhwGameOptions(PerGameCommonOptions):
    required_weapon_categories: RequiredWeaponCategories