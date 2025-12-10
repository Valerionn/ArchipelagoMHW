from worlds.mhw.game_id import mhw_weapon_id

gunlance_weapon_category = 7


def get_id(base_id):
    return mhw_weapon_id + gunlance_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(Lance,-Gunlance)
gunlance_by_rarity = {
    0: {
#        get_id(10): "Iron Gunlance I",
        get_id(11): "Iron Gunlance II",
        get_id(44): "Bone Gunlance I",
        get_id(45): "Bone Gunlance II",
    },
    1: {
        get_id(12): "Iron Gunlance III",
        get_id(20): "Pulsar Gunlance I",
        get_id(34): "Madness Gunlance I",
        get_id(46): "Bone Gunlance III",
        get_id(54): "Jagras Gunlance I",
        get_id(67): "Carapace Cannon I",
    },
    2: {
        get_id(13): "Steel Gunlance I",
        get_id(21): "Pulsar Gunlance II",
        get_id(30): "Princess Panoply",
        get_id(35): "Madness Gunlance II",
        get_id(47): "Bone Cannon I",
        get_id(55): "Jagras Gunlance II",
        get_id(60): "Girros Gunlance I",
        get_id(68): "Carapace Cannon II",
        get_id(73): "Blazing Gunlance I",
        get_id(78): "Dragonbone Gunlance I",
    },
    3: {
        get_id(14): "Steel Gunlance II",
        get_id(22): "Pulsar Gunlance III",
        get_id(25): "Rath Gunlance I",
        get_id(36): "Madness Gunlance III",
        get_id(40): "Glacial Gunlance I",
        get_id(48): "Bone Cannon II",
        get_id(56): "Jagras Gunlance III",
        get_id(61): "Girros Gunlance II",
        get_id(69): "Carapace Cannon III",
        get_id(74): "Blazing Gunlance II",
        get_id(79): "Dragonbone Gunlance II",
    }
}
