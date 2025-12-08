from worlds.mhw.game_id import mhw_weapon_id

light_bowgun_weapon_category = 13


def get_id(base_id):
    return mhw_weapon_id + light_bowgun_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(Bow,-LBG,-HBG)
light_bowguns_by_rarity = {
    0: {
        get_id(10): "Chain Blitz I",
        get_id(11): "Chain Blitz II",
        get_id(43): "Hunter's Rifle I",
        get_id(44): "Hunter's Rifle II",
    },
    1: {
        get_id(12): "Chain Blitz III",
        get_id(27): "Jagras Blitz I",
        get_id(45): "Hunter's Rifle III",
        get_id(58): "Madness Rifle I",
        get_id(66): "Carapace Rifle I",
    },
    2: {
        get_id(13): "High Chain Blitz I",
        get_id(20): "Lumu Blitz I",
        get_id(28): "Jagras Blitz II",
        get_id(38): "Thunder Blitz I",
        get_id(46): "Power Rifle I",
        get_id(53): "Blazing Rifle I",
        get_id(59): "Madness Rifle II",
        get_id(67): "Carapace Rifle II",
        get_id(89): "Dragonbone Bow I",
    },
    3: {
        get_id(14): "High Chain Blitz II",
        get_id(21): "Lumu Blitz II",
        get_id(29): "Jagras Blitz III",
        get_id(33): "Flame Blitz I",
        get_id(39): "Thunder Blitz II",
        get_id(91): "Snow Blitz I",
        get_id(47): "Power Rifle II",
        get_id(54): "Blazing Rifle II",
        get_id(60): "Madness Rifle III",
        get_id(68): "Carapace Rifle III",
        get_id(72): "Garon Rifle I",
        get_id(81): "Mythical Horn",
        get_id(90): "Dragonbone Bow II",
    }
}
