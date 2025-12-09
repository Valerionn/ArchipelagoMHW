from BaseClasses import Item
from .armrs.armors import armors_by_rarity
from .itms.bow import bows_by_rarity
from .itms.charge_blade import charge_blades_by_rarity
from .itms.dual_blades import dual_blades_by_rarity
from .game_id import mhw_name
from .itms.greatsword import great_swords_by_rarity
from .itms.gunlance import gunlance_by_rarity
from .itms.hammer import hammers_by_rarity
from .itms.heavy_bowgun import heavy_bowguns_by_rarity
from .itms.hunting_horn import hunting_horns_by_rarity
from .itms.insect_glaive import insect_glaives_by_rarity
from .itms.lance import lances_by_rarity
from .itms.light_bowgun import light_bowguns_by_rarity
from .itms.longsword import long_swords_by_rarity
from .itms.switch_axe import switch_axes_by_rarity
from .itms.swordandshield import swordandshields_by_rarity


class MhwItem(Item):
    game = mhw_name


dual_blades = {
    k: name
    for _, rarity_dict in dual_blades_by_rarity.items()
    for k, name in rarity_dict.items()
}
great_swords = {
    k: name
    for _, rarity_dict in great_swords_by_rarity.items()
    for k, name in rarity_dict.items()
}
long_swords = {
    k: name
    for _, rarity_dict in long_swords_by_rarity.items()
    for k, name in rarity_dict.items()
}
swordandshields = {
    k: name
    for _, rarity_dict in swordandshields_by_rarity.items()
    for k, name in rarity_dict.items()
}
gunlances = {
    k: name
    for _, rarity_dict in gunlance_by_rarity.items()
    for k, name in rarity_dict.items()
}
bows = {
    k: name
    for _, rarity_dict in bows_by_rarity.items()
    for k, name in rarity_dict.items()
}
hammers = {
    k: name
    for _, rarity_dict in hammers_by_rarity.items()
    for k, name in rarity_dict.items()
}
hunting_horns = {
    k: name
    for _, rarity_dict in hunting_horns_by_rarity.items()
    for k, name in rarity_dict.items()
}
lances = {
    k: name
    for _, rarity_dict in lances_by_rarity.items()
    for k, name in rarity_dict.items()
}
switch_axes = {
    k: name
    for _, rarity_dict in switch_axes_by_rarity.items()
    for k, name in rarity_dict.items()
}
charge_blades = {
    k: name
    for _, rarity_dict in charge_blades_by_rarity.items()
    for k, name in rarity_dict.items()
}
heavy_bowguns = {
    k: name
    for _, rarity_dict in heavy_bowguns_by_rarity.items()
    for k, name in rarity_dict.items()
}
light_bowguns = {
    k: name
    for _, rarity_dict in light_bowguns_by_rarity.items()
    for k, name in rarity_dict.items()
}
insect_glaives = {
    k: name
    for _, rarity_dict in insect_glaives_by_rarity.items()
    for k, name in rarity_dict.items()
}
armors = {
    k: name
    for _, rarity_dict in armors_by_rarity.items()
    for k, name in rarity_dict.items()
}

item_table = {
    **dual_blades,
    **great_swords,
    **long_swords,
    **swordandshields,
    **gunlances,
    **bows,
    **hammers,
    **hunting_horns,
    **lances,
    **switch_axes,
    **charge_blades,
    **heavy_bowguns,
    **light_bowguns,
    **insect_glaives,
    **armors
}

item_name_groups = {
    "Dual Blades": {name for name in dual_blades.values()},
    "Greatsword": {name for name in great_swords.values()},
    "Longsword": {name for name in long_swords.values()},
    "Sword and Shield": {name for name in swordandshields.values()},
    "Gun Lance": {name for name in gunlances.values()},
    "Bow": {name for name in bows.values()},
    "Hammer": {name for name in hammers.values()},
    "Hunting Horn": {name for name in hunting_horns.values()},
    "Lance": {name for name in lances.values()},
    "Switch Axe": {name for name in switch_axes.values()},
    "Charge Blade": {name for name in charge_blades.values()},
    "Heavy Bowgun": {name for name in heavy_bowguns.values()},
    "Light Bowgun": {name for name in light_bowguns.values()},
    "Insect Glaive": {name for name in insect_glaives.values()},
    "Armors": {name for name in armors.values()},
}


def combine_by_rarity(*dicts):
    combined = {}

    for d in dicts:
        for rarity, items in d.items():
            if rarity not in combined:
                combined[rarity] = {}
            combined[rarity].update(items)

    return combined


weapons_by_rarity = combine_by_rarity(
    dual_blades_by_rarity, great_swords_by_rarity, long_swords_by_rarity, swordandshields_by_rarity, gunlance_by_rarity,
    bows_by_rarity, hammers_by_rarity, hunting_horns_by_rarity, lances_by_rarity, switch_axes_by_rarity,
    charge_blades_by_rarity, heavy_bowguns_by_rarity, light_bowguns_by_rarity, insect_glaives_by_rarity
)
