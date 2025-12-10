from worlds.mhw.game_id import mhw_weapon_id

insect_glaives_weapon_category = 10


def get_id(base_id):
    return mhw_weapon_id + insect_glaives_weapon_category * 1000 + base_id

# https://mhw.poedb.tw/eng/wp_weapon
insect_glaives_by_rarity = {
    0: {
 #       get_id(10): "Iron Blade I",
        get_id(11): "Iron Blade II",
        get_id(48): "Bone Rod I",
        get_id(49): "Bone Rod II",
    },
    1: {
        get_id(12): "Iron Blade III",
        get_id(25): "Kulu Blade I",
        get_id(40): "Blooming Glaive I",
        get_id(50): "Bone Rod III",
        get_id(61): "Aqua Rod I",
        get_id(72): "Pulsar Rod I",
    },
    2: {
        get_id(13): "Steel Blade I",
        get_id(26): "Kulu Blade II",
        get_id(31): "Luminous Blade I",
        get_id(41): "Blooming Glaive II",
        get_id(51): "Hard Bone Rod I",
        get_id(51): "Flammenkaefer",
        get_id(73): "Pulsar Rod II",
        get_id(82): "Dragonbone Glaive I",
    },
    3: {
        get_id(14): "Steel Blade II",
        get_id(20): "Flame Glaive I",
        get_id(27): "Kulu Blade III",
        get_id(32): "Luminous Blade II",
        get_id(36): "Frost Blade I",
        get_id(42): "Blooming Glaive III",
        get_id(52): "Hard Bone Rod II",
        get_id(63): "Aqua Rod III",
        get_id(67): "Diablos Rod I",
        get_id(74): "Pulsar Rod III",
        get_id(78): "Garon Rod I",
        get_id(83): "Dragonbone Glaive II",
        get_id(85): "Indigo Flash",
    }
}
