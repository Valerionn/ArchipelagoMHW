from worlds.mhw.game_id import mhw_weapon_id

long_sword_weapon_category = 3


def get_id(base_id):
    return mhw_weapon_id + long_sword_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(Longsword,-Hammer,-Hunting-Horn)
long_swords_by_rarity = {
    0: {
#        get_id(10): "Iron Katana I",
        get_id(11): "Iron Katana II",
        get_id(41): "Bone Shotel I",
        get_id(42): "Bone Shotel II",
    },
    1: {
        get_id(12): "Iron Katana III",
        get_id(25): "First Dance I",
        get_id(43): "Bone Shotel III",
        get_id(56): "Jyura Shotel I",
        get_id(64): "Pulsar Shotel I",
    },
    2: {
        get_id(13): "Iron Grace I",
        get_id(20): "Flickering Glow I",
        get_id(26): "First Dance II",
        get_id(33): "Wyvern Blade Leaf",
        get_id(44): "Hard Bone Shotel I",
        get_id(51): "Blazing Shotel I",
        get_id(57): "Jyura Shotel II",
        get_id(65): "Pulsar Shotel II",
        get_id(74): "Dark Shotel I",
        get_id(79): "Dragonbone Stabber I",
        get_id(93): "Azure Star Blade",
    },
    3: {
        get_id(9): "Iron Grace II",
        get_id(14): "Iron Grace II",
        get_id(21): "Flickering Glow II",
        get_id(27): "First Dance III",
        get_id(37): "Wyvern Blade Fall",
        get_id(45): "Hard Bone Shotel II",
        get_id(52): "Blazing Shotel II",
        get_id(58): "Jyura Shotel III",
        get_id(66): "Pulsar Shotel III",
        get_id(70): "Glacial Shotel I",
        get_id(75): "Dark Shotel II",
        get_id(80): "Dragonbone Stabber II",
    }
}
