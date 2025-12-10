from worlds.mhw.game_id import mhw_weapon_id

swordandshield_weapon_category = 1


def get_id(base_id):
    return mhw_weapon_id + swordandshield_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(GS,-SnS,-DB)
swordandshields_by_rarity = {
    0: {
#        get_id(10): "Hunter's Knife I",
        get_id(11): "Hunter's Knife II",
        get_id(46): "Bone Kukri I",
        get_id(47): "Bone Kukri II",
    },
    1: {
        get_id(12): "Hunter's Knife III",
        get_id(25): "Aqua Messer I",
        get_id(35): "Blooming Knife I",
        get_id(48): "Bone Kukri III",
        get_id(63): "Jagras Edge I",
        get_id(73): "Carapace Edge I",
    },
    2: {
        get_id(13): "Steel Knife I",
        get_id(26): "Aqua Messer II",
        get_id(31): "Princess Rapier",
        get_id(36): "Blooming Knife II",
        get_id(41): "Lumu Knife I",
        get_id(49): "Chief Kukri I",
        get_id(58): "Thunder Edge I",
        get_id(64): "Jagras Edge II",
        get_id(69): "Blazing Edge I",
        get_id(74): "Carapace Edge II",
        get_id(79): "Spiked Edge I",
        get_id(84): "Dragonbone Sword I",
        get_id(98): "Girros Knife I",
    },
    3: {
        get_id(14): "Steel Knife II",
        get_id(20): "Flame Knife I",
        get_id(27): "Aqua Messer III",
        get_id(37): "Blooming Knife III",
        get_id(42): "Lumu Knife II",
        get_id(50): "Chief Kukri II",
        get_id(54): "Glacial Grace I",
        get_id(59): "Thunder Edge II",
        get_id(65): "Jagras Edge III",
        get_id(70): "Blazing Edge II",
        get_id(75): "Carapace Edge III",
        get_id(80): "Spiked Edge II",
        get_id(85): "Dragonbone Sword II",
        get_id(87): "Fulminator",
        get_id(97): "Heavy Bang",
        get_id(99): "Girros Knife II",
    }
}
