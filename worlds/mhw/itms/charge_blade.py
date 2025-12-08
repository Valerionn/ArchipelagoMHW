from worlds.mhw.game_id import mhw_weapon_id

charge_blade_weapon_category = 9


def get_id(base_id):
    return mhw_weapon_id + charge_blade_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(SA,-CB)
charge_blades_by_rarity = {
    0: {
        get_id(10): "Proto Commission Axe I",
        get_id(11): "Proto Commission Axe II",
        get_id(39): "Bone Strongarm I",
        get_id(40): "Bone Strongarm II",
    },
    1: {
        get_id(12): "Proto Commission Axe III",
        get_id(25): "Mudslide Blade I",
        get_id(41): "Bone Strongarm III",
        get_id(52): "Jagras Strongarm I",
        get_id(67): "Pulsar Strongarm I",
    },
    2: {
        get_id(13): "Elite Commission Axe I",
        get_id(26): "Mudslide Blade II",
        get_id(35): "Dear Lutemis",
        get_id(42): "Hard Bone Strongarm I",
        get_id(53): "Jagras Strongarm II",
        get_id(60): "Girros Strongarm I",
        get_id(68): "Pulsar Strongarm II",
        get_id(77): "Dragonbone Cutter I",
    },
    3: {
        get_id(14): "Elite Commission Axe II",
        get_id(20): "Rathsblade I",
        get_id(27): "Mudslide Blade III",
        get_id(31): "Everfrost Blade I",
        get_id(43): "Hard Bone Strongarm II",
        get_id(47): "Diablos Wall I",
        get_id(53): "Jagras Strongarm III",
        get_id(61): "Girros Strongarm II",
        get_id(69): "Pulsar Strongarm III",
        get_id(73): "Garon Strongarm I",
        get_id(78): "Dragonbone Cutter II",
    }
}
