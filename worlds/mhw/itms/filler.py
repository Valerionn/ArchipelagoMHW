from worlds.mhw.game_id import filler_item_id


def get_id(base_id):
    return filler_item_id + base_id

filler_items = {
    get_id(1): "Ammo Bundle R1",
    get_id(2): "Ammo Bundle R2",
    get_id(3): "Ammo Bundle R3",
    get_id(4): "Ammo Bundle R4",
    get_id(10): "Healing Item Bundle",
    get_id(24): "Armor Sphere Bundle",
    get_id(25): "Armor Sphere+ Bundle",
    get_id(26): "Advanced Armor Sphere Bundle",
    get_id(27): "Hard Armor Sphere Bundle",
    get_id(28): "Heavy Armor Sphere Bundle",
}