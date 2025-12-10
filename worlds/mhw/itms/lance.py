from worlds.mhw.game_id import mhw_weapon_id

lance_weapon_category = 6


def get_id(base_id):
    return mhw_weapon_id + lance_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(Lance,-Gunlance)
lances_by_rarity = {
    0: {
#        get_id(10): "Iron Lance I",
        get_id(11): "Iron Lance II",
        get_id(44): "Bone Lance I",
        get_id(45): "Bone Lance II",
    },
    1: {
        get_id(12): "Iron Lance III",
        get_id(20): "Kulu Lance I",
        get_id(33): "Blooming Lance I",
        get_id(46): "Bone Lance III",
        get_id(58): "Carapace Lance I",
        get_id(64): "Aqua Horn I",
    },
    2: {
        get_id(13): "Steel Lance I",
        get_id(21): "Kulu Lance II",
        get_id(28): "Thunder Lance I",
        get_id(34): "Blooming Lance II",
        get_id(47): "Hard Bone Lance I",
        get_id(59): "Carapace Lance II",
        get_id(65): "Aqua Horn II",
        get_id(74): "Taurus Lance I",
        get_id(79): "Dragonbone Lance I",
    },
    3: {
        get_id(14): "Steel Lance II",
        get_id(22): "Kulu Lance III",
        get_id(29): "Thunder Lance II",
        get_id(35): "Blooming Lance III",
        get_id(39): "Flame Lance I",
        get_id(48): "Hard Bone Lance II",
        get_id(54): "Garon Lance I",
        get_id(60): "Carapace Lance III",
        get_id(66): "Aqua Horn III",
        get_id(70): "Glacial Lance I",
        get_id(75): "Taurus Lance II",
        get_id(80): "Dragonbone Lance II",
        get_id(91): "Thunderpike",
    }
}
