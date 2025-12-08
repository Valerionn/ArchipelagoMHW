import random

from BaseClasses import ItemClassification
from Utils import visualize_regions
from worlds.AutoWorld import World
from worlds.generic.Rules import add_rule, set_rule
from .armrs.armors import armor_sets_by_rarity, armors_by_rarity
from .items import item_table, item_name_groups, MhwItem
from .itms.bow import bows_by_rarity
from .itms.dual_blades import dual_blades_by_rarity
from .itms.greatsword import great_swords_by_rarity
from .itms.gunlance import gunlance_by_rarity
from .itms.longsword import long_swords_by_rarity
from .itms.swordandshield import swordandshields_by_rarity
from .locations import location_table, location_name_groups
from .options import MhwGameOptions
from .regions import create_regions


class MhwWorld(World):
    """Insert description of the world/game here."""
    game = "Monster Hunter World"  # name of the game/world
    options_dataclass = MhwGameOptions  # options the player can set
    options: MhwGameOptions  # typing hints for option results

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for
                       id, name in item_table.items()}
    location_name_to_id = {name: id for
                           id, name in location_table.items()}

    location_name_groups = location_name_groups
    item_name_groups = item_name_groups

    relevant_items_for_rarity = {}


    def generate_early(self) -> None:
        relevant_items_per_rarity = {}

    def create_regions(self) -> None:
        create_regions(self)

    def create_item(self, name: str) -> MhwItem:
        classification = ItemClassification.useful
        return MhwItem(name, classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        used_items = set()
        item_pool = []
        # Necessary progression items
        for rarity in range(4):
            weapons = random.choice([dual_blades_by_rarity, great_swords_by_rarity, long_swords_by_rarity])[rarity]
            weapon_id, weapon_name = random.choice(list(weapons.items()))
            used_items.add(weapon_name)
            item_pool.append(MhwItem(weapon_name, ItemClassification.progression, weapon_id, self.player))
            self.relevant_items_for_rarity[rarity] = {weapon_name}
            for offset in range(5):
                armor_set_id = random.choice(list(armor_sets_by_rarity[rarity].keys()))
                armor_id = armor_set_id + offset
                armor_name = armors_by_rarity[rarity][armor_id]
                used_items.add(armor_name)
                item_pool.append(MhwItem(armor_name, ItemClassification.progression, armor_id, self.player))
                self.relevant_items_for_rarity[rarity].add(armor_name)


        for name in self.item_name_to_id:
            if name in used_items:
                continue
            item_pool.append(self.create_item(name))

        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        item_pool += [self.create_filler() for _ in range(total_locations - len(item_pool))]

        self.multiworld.itempool += item_pool

    def set_rules(self) -> None:
        weapons_by_rarity1 = ([k for k in dual_blades_by_rarity[1].values()] 
                              + [k for k in bows_by_rarity[1].values()]  
                              + [k for k in great_swords_by_rarity[1].values()]
                              + [k for k in long_swords_by_rarity[1].values()]
                              + [k for k in swordandshields_by_rarity[1].values()]
                              + [k for k in gunlance_by_rarity[1].values()])
        weapons_by_rarity2 = ([k for k in dual_blades_by_rarity[2].values()] 
                              + [k for k in bows_by_rarity[2].values()]  
                              + [k for k in great_swords_by_rarity[2].values()]
                              + [k for k in long_swords_by_rarity[2].values()]
                              + [k for k in swordandshields_by_rarity[2].values()]
                              + [k for k in gunlance_by_rarity[2].values()])
        weapons_by_rarity3 = ([k for k in dual_blades_by_rarity[3].values()] 
                              + [k for k in bows_by_rarity[3].values()]  
                              + [k for k in great_swords_by_rarity[3].values()]
                              + [k for k in long_swords_by_rarity[3].values()]
                              + [k for k in swordandshields_by_rarity[3].values()]
                              + [k for k in gunlance_by_rarity[3].values()])

        set_rule(self.multiworld.get_entrance("Three Stars", self.player), lambda state: any(state.has(item, self.player) for item in weapons_by_rarity1))
        set_rule(self.multiworld.get_entrance("Four Stars", self.player), lambda state: any(state.has(item, self.player) for item in weapons_by_rarity2))
        set_rule(self.multiworld.get_entrance("Five Stars", self.player), lambda state: any(state.has(item, self.player) for item in weapons_by_rarity3))
