from worlds.mhw.game_id import mhw_weapon_id

hammer_weapon_category = 4


def get_id(base_id):
    return mhw_weapon_id + hammer_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(Longsword,-Hammer,-Hunting-Horn)
hammers_by_rarity = {
    0: {
        get_id(10): "Iron Hammer I",
        get_id(11): "Iron Hammer II",
        get_id(39): "Bone Bludgeon I",
        get_id(40): "Bone Bludgeon II",
    },
    1: {
        get_id(12): "Iron Hammer III",
        get_id(23): "Aqua Hammer I",
        get_id(34): "Blooming Hammer I",
        get_id(41): "Bone Bludgeon III",
        get_id(49): "Bone Spike I",
        get_id(56): "Kulu Beak I",
        get_id(67): "Carapace Sledge I",
    },
    2: {
        get_id(13): "Iron Demon I",
        get_id(24): "Aqua Hammer II",
        get_id(29): "Girros Hammer I",
        get_id(35): "Blooming Hammer II",
        get_id(42): "Fossil Bludgeon I",
        get_id(50): "Bone Spike II",
        get_id(57): "Kulu Beak II",
        get_id(68): "Carapace Sledge II",
        get_id(73): "Blazing Hammer I",
        get_id(78): "Dragonbone Basher I",
        get_id(89): "Thunder Hammer I",
        get_id(130): "Bristly Pincushion",
    },
    3: {
        get_id(14): "Iron Demon II",
        get_id(20): "Frozen Core",
        get_id(25): "Aqua Hammer III",
        get_id(30): "Girros Hammer II",
        get_id(36): "Blooming Hammer III",
        get_id(43): "Fossil Bludgeon II",
        get_id(58): "Kulu Beak III",
        get_id(62): "Diablos Sledge I",
        get_id(69): "Carapace Sledge III",
        get_id(74): "Blazing Hammer II",
        get_id(79): "Dragonbone Basher II",
        get_id(90): "Thunder Hammer II",
    }
}
