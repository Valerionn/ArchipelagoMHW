from worlds.mhw.game_id import mhw_weapon_id

bow_weapon_category = 11


def get_id(base_id):
    return mhw_weapon_id + bow_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(Bow,-LBG,-HBG)
bows_by_rarity = {
    0: {
        get_id(20): "Iron Bow I",
        get_id(21): "Iron Bow II",
        get_id(58): "Hunter's Bow I",
        get_id(59): "Hunter's Bow II",
    },
    1: {
        get_id(22): "Iron Bow III",
        get_id(30): "Kulu Arrow I",
        get_id(48): "Aqua Arrow I",
        get_id(60): "Hunter's Bow III",
        get_id(73): "Blooming Arch I",
        get_id(84): "Pulsar Bow I",
    },
    2: {
        get_id(23): "Steel Bow I",
        get_id(31): "Kulu Arrow II",
        get_id(38): "Princess Arrow I",
        get_id(49): "Aqua Arrow II",
        get_id(61): "Hunter's Stoutbow I",
        get_id(74): "Blooming Arch II",
        get_id(79): "Blazing Bow I",
        get_id(85): "Pulsar Bow II",
        get_id(89): "Dragonbone Bow I",
    },
    3: {
        get_id(24): "Steel Bow II",
        get_id(32): "Kulu Arrow III",
        get_id(43): "Rathslinger I",
        get_id(50): "Aqua Arrow III",
        get_id(54): "Glacial Arrow I",
        get_id(62): "Hunter's Stoutbow II",
        get_id(68): "Diablos Bow I",
        get_id(75): "Blooming Arch III",
        get_id(80): "Blazing Bow II",
        get_id(86): "Pulsar Bow III",
        get_id(90): "Dragonbone Bow II",
    }
}
