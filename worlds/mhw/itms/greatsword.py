from worlds.mhw.game_id import mhw_weapon_id

great_sword_weapon_category = 0


def get_id(base_id):
    return mhw_weapon_id + great_sword_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(GS,-SnS,-DB)
great_swords_by_rarity = {
    0: {
#        get_id(10): "Buster Sword I",
        get_id(11): "Buster Sword II",
        get_id(49): "Bone Blade I",
        get_id(50): "Bone Blade II",
    },
    1: {
        get_id(12): "Buster Sword III",
        get_id(25): "Jagras Blade I",
        get_id(38): "Blooming Blade I",
        get_id(51): "Bone Blade III",
        get_id(62): "Aqua Slasher I",
        get_id(68): "Carapace Buster I",
    },
    2: {
        get_id(13): "Buster Blade I",
        get_id(20): "Thunder Blade I",
        get_id(26): "Jagras Blade II",
        get_id(31): "Girros Blade I",
        get_id(39): "Blooming Blade II",
        get_id(52): "Bone Slasher I",
        get_id(59): "Flammenzahn",
        get_id(63): "Aqua Slasher II",
        get_id(69): "Carapace Buster II",
        get_id(74): "Spiked Blade I",
        get_id(79): "Dragonbone Cleaver I",
    },
    3: {
        get_id(9): "Wyvern Ignition Steel",
        get_id(14): "Buster Blade II",
        get_id(21): "Thunder Blade II",
        get_id(27): "Jagras Blade III",
        get_id(32): "Girros Blade II",
        get_id(40): "Blooming Blade III",
        get_id(44): "Flame Blade I",
        get_id(53): "Bone Slasher II",
        get_id(64): "Aqua Slasher III",
        get_id(70): "Carapace Buster III",
        get_id(75): "Spiked Blade II",
        get_id(80): "Dragonbone Cleaver II",
        get_id(83): "Thundersword",
        get_id(94): "Freeze Blade I",
    }
}
