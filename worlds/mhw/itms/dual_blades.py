from worlds.mhw.game_id import mhw_weapon_id

dual_blades_weapon_category = 2


def get_id(base_id):
    return mhw_weapon_id + dual_blades_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(GS,-SnS,-DB)
dual_blades_by_rarity = {
    0: {
#        get_id(10): "Matched Slicers I",
        get_id(11): "Matched Slicers II",
        get_id(40): "Bone Hatchets I",
        get_id(41): "Bone Hatchets II",
    },
    1: {
        get_id(12): "Matched Slicers III",
        get_id(31): "Rending Beaks I",
        get_id(42): "Bone Hatchets III",
        get_id(60): "Madness Pangas I",
        get_id(73): "Pulsar Hatchets I",
    },
    2: {
        get_id(13): "Dual Slicers I",
        get_id(20): "Luminous Daggers I",
        get_id(32): "Rending Beaks II",
        get_id(37): "Sworn Rapiers",
        get_id(43): "Wild Hatchets I",
        get_id(50): "Blazing Hatchets I",
        get_id(61): "Madness Pangas II",
        get_id(68): "Taurus Pangas I",
        get_id(74): "Pulsar Hatchets II",
        get_id(83): "Dragonbone Twinblades I",
        get_id(128): "Downy Crake Brooms",
    },
    3: {
        get_id(14): "Dual Slicers II",
        get_id(21): "Luminous Daggers II",
        get_id(27): "Freeze Daggers I",
        get_id(33): "Rending Beaks III",
        get_id(44): "Wild Hatchets II",
        get_id(51): "Blazing Hatchets II",
        get_id(55): "Diablos Hatchets I",
        get_id(62): "Madness Pangas III",
        get_id(69): "Taurus Pangas II",
        get_id(75): "Pulsar Hatchets III",
        get_id(79): "Garon Hatchets I",
        get_id(84): "Dragonbone Twinblades II",
        get_id(87): "Kirin Bolts",
    }
}
