from worlds.mhw.game_id import mhw_weapon_id

switch_axe_weapon_category = 8


def get_id(base_id):
    return mhw_weapon_id + switch_axe_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(SA,-CB)
switch_axes_by_rarity = {
    0: {
        get_id(10): "Proto Iron Axe I",
        get_id(11): "Proto Iron Axe II",
        get_id(38): "Bone Axe I",
        get_id(39): "Bone Axe II",
    },
    1: {
        get_id(12): "Proto Iron Axe III",
        get_id(27): "Jagras Axe I",
        get_id(40): "Bone Axe III",
        get_id(57): "Madness Axe I",
        get_id(65): "Carapace Axe I",
    },
    2: {
        get_id(13): "Improved Steel Axe I",
        get_id(20): "Thunder Axe I",
        get_id(28): "Jagras Axe II",
        get_id(41): "Bone Smasher I",
        get_id(48): "Lumu Axe I",
        get_id(58): "Madness Axe II",
        get_id(66): "Carapace Axe II",
        get_id(76): "Flammenbeil",
        get_id(79): "Dragonbone Slicer I",
    },
    3: {
        get_id(14): "Improved Steel Axe II",
        get_id(21): "Thunder Axe II",
        get_id(29): "Jagras Axe III",
        get_id(33): "Rathalos Axe I",
        get_id(42): "Bone Smasher II",
        get_id(49): "Lumu Axe II",
        get_id(53): "Glacial Axe I",
        get_id(59): "Madness Axe III",
        get_id(67): "Carapace Axe III",
        get_id(71): "Diablos Axe I",
        get_id(80): "Dragonbone Slicer II",
        get_id(82): "Peal",
    }
}
