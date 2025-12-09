from ..game_id import mhw_armor_id

def get_id(base_id):
    return mhw_armor_id + base_id * 10

# https://mhw.poedb.tw/eng/pl_equip
armor_sets_by_rarity = {
    0: {
        get_id(2): "Leather",
        get_id(1): "Hunter",
        get_id(4): "Jagras",
        get_id(5): "Bone",
        # get_id(8): "Gajau", # Legs only
        get_id(9): "Vespoid",
        get_id(10): "Kulu",
        get_id(15): "Chainmail",
    },
    1: {
        get_id(6): "Alloy",
        get_id(11): "Pukei",
        get_id(12): "Jyura",
        get_id(13): "Barroth",
        get_id(14): "Kadachi",
    },
    2: {
        get_id(3): "Anja",
        get_id(18): "Hornetaur",
        get_id(21): "Rathian",
        get_id(22): "Girros",
        get_id(23): "Tzitzi",
        get_id(24): "Lumu",
        get_id(25): "High Metal",
        get_id(28): "Baan",
    },
    3: {
        get_id(26): "Death Stench",
        get_id(27): "Legiana",
        get_id(29): "Odogaron",
        get_id(31): "Ingot",
        get_id(33): "Rathalos",
        get_id(34): "Diablos",
        get_id(35): "Kirin",
        get_id(36): "Brigade",
    }
}

ARMOR_SUFFIXES = ["Helm", "Mail", "Vambrace", "Coil", "Greaves"]
armors_by_rarity = {}
for rarity, items in armor_sets_by_rarity.items():
    new_items = {}
    for base_id, name in items.items():
        for offset, suffix in enumerate(ARMOR_SUFFIXES):
            new_items[base_id + offset] = f"{name} {suffix}"
    armors_by_rarity[rarity] = new_items
