from worlds.mhw.game_id import mhw_weapon_id

heavy_bowgun_weapon_category = 12


def get_id(base_id):
    return mhw_weapon_id + heavy_bowgun_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(Bow,-LBG,-HBG)
heavy_bowguns_by_rarity = {
    0: {
#        get_id(20): "Iron Assault I",
        get_id(21): "Iron Assault II",
        get_id(54): "Bone Shooter I",
        get_id(55): "Bone Shooter II",
    },
    1: {
        get_id(22): "Iron Assault III",
        get_id(30): "Aqua Assault I",
        get_id(44): "Jagras Assault I",
        get_id(56): "Bone Shooter III",
        get_id(67): "Blooming Shooter I",
        get_id(80): "Pulsar Shooter I",
    },
    2: {
        get_id(23): "Steel Assault I",
        get_id(31): "Aqua Assault II",
        get_id(36): "Luminous Assault I",
        get_id(45): "Jagras Assault II",
        get_id(50): "Blazing Assault I",
        get_id(57): "Heavy Shooter I",
        get_id(68): "Blooming Shooter II",
        get_id(73): "Spiked Shooter I",
        get_id(81): "Pulsar Shooter II",
        get_id(86): "Dragonbone Cannon I",
    },
    3: {
        get_id(24): "Steel Assault II",
        get_id(32): "Aqua Assault III",
        get_id(37): "Luminous Assault II",
        get_id(41): "Shattercryst",
        get_id(46): "Jagras Assault III",
        get_id(51): "Blazing Assault II",
        get_id(58): "Heavy Shooter II",
        get_id(61): "Diablos Shooter I",
        get_id(69): "Blooming Shooter III",
        get_id(74): "Spiked Shooter II",
        get_id(82): "Pulsar Shooter III",
        get_id(87): "Dragonbone Cannon II",
        get_id(90): "Quickcaster",
    }
}
