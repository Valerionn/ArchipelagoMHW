import math
import os.path
from typing import Mapping, Any

from BaseClasses import ItemClassification, Item
from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule
from .armrs.armors import armor_sets_by_rarity, armors_by_rarity
from .containers import MhwContainer
from .items import item_table, item_name_groups, MhwItem, weapons_by_rarity
from .itms.bow import bows_by_rarity
from .itms.dual_blades import dual_blades_by_rarity
from .itms.filler import filler_items
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
    randomizer_seed = 0
    max_rarity = 8

    def generate_early(self) -> None:
        self.randomizer_seed = self.random.getrandbits(32)

    def create_regions(self) -> None:
        create_regions(self)

    def create_item(self, name: str) -> MhwItem:
        classification = ItemClassification.useful
        return MhwItem(name, classification, self.item_name_to_id[name], self.player)

    def choose_rarity(self, weight_by_rarity, weight_sum):
        roll = self.random.random() * weight_sum
        cumulative = 0
        for r, w in weight_by_rarity.items():
            cumulative += w
            if roll <= cumulative:
                return r
        return 0

    def create_filler(self) -> "Item":
        filler_id, filler_name = self.random.choice(list(filler_items.items()))
        return MhwItem(filler_name, ItemClassification.filler, filler_id, self.player)

    def create_items(self) -> None:
        used_items = set()
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        item_pool = []
        # Necessary progression items - at least 1 weapon per rarity, and at least 1 armor piece per rarity
        for rarity in range(self.max_rarity):
            weapon_id, weapon_name = self.random.choice(list(weapons_by_rarity[rarity].items()))
            used_items.add(weapon_name)
            item_pool.append(MhwItem(weapon_name, ItemClassification.progression, weapon_id, self.player))
            for offset in range(5):
                armor_set_id = self.random.choice(list(armor_sets_by_rarity[rarity].keys()))
                armor_id = armor_set_id + offset
                armor_name = armors_by_rarity[rarity][armor_id]
                used_items.add(armor_name)
                item_pool.append(MhwItem(armor_name, ItemClassification.progression, armor_id, self.player))

        # Add filler items - at least enough for our own excluded locations
        for _ in range(75):
            item_pool.append(self.create_filler())

        # Weight that favors lower rarity equipment
        weight_sum = 0
        weight_by_rarity = {}
        for rarity in range(self.max_rarity):
            weight = self.max_rarity - rarity
            weight_sum += weight
            weight_by_rarity[rarity] = weight

        # Add weapons
        items_needed = total_locations - len(item_pool)
        additional_weapons_needed = math.ceil(items_needed / 3.0)
        additional_weapons_added = 0

        while additional_weapons_added < additional_weapons_needed:
            rarity = self.choose_rarity(weight_by_rarity, weight_sum)
            weapon_id, weapon_name = self.random.choice(list(weapons_by_rarity[rarity].items()))
            if weapon_name in used_items:
                continue
            additional_weapons_added += 1
            used_items.add(weapon_name)
            item_pool.append(MhwItem(weapon_name, ItemClassification.useful, weapon_id, self.player))

        # Add armor
        items_needed = total_locations - len(item_pool)
        additional_armors_added = 0
        while additional_armors_added < items_needed:
            rarity = self.choose_rarity(weight_by_rarity, weight_sum)
            offset = self.random.randrange(0, 5)
            armor_set_id = self.random.choice(list(armor_sets_by_rarity[rarity].keys()))
            armor_id = armor_set_id + offset
            armor_name = armors_by_rarity[rarity][armor_id]
            if armor_name in used_items:
                continue
            additional_armors_added += 1
            used_items.add(armor_name)
            item_pool.append(MhwItem(armor_name, ItemClassification.useful, armor_id, self.player))

        item_pool += [self.create_filler() for _ in range(total_locations - len(item_pool))]

        self.multiworld.itempool += item_pool

    def has_rarity_weapon(self, state, rarity: int):
        # Higher rarity weapons would be okay too, but we want to encourage the randomizer to not drop a rarity 8 weapon immediately
        return any(state.has(item, self.player) for item in weapons_by_rarity[rarity].values())

    def set_rules(self) -> None:
        # Low Rank - up to rarity 4 weapons (0-indexed)
        set_rule(self.multiworld.get_entrance("3 Stars", self.player), lambda state: self.has_rarity_weapon(state, 1))
        set_rule(self.multiworld.get_entrance("4 Stars", self.player), lambda state: self.has_rarity_weapon(state, 2))
        set_rule(self.multiworld.get_entrance("5 Stars", self.player), lambda state: self.has_rarity_weapon(state, 3))
        # High Rank - up to rarity 8 weapons (0-indexed)
        set_rule(self.multiworld.get_entrance("6 Stars", self.player), lambda state: self.has_rarity_weapon(state, 4))
        set_rule(self.multiworld.get_entrance("7 Stars", self.player), lambda state: self.has_rarity_weapon(state, 5))
        set_rule(self.multiworld.get_entrance("8 Stars", self.player), lambda state: self.has_rarity_weapon(state, 6))
        set_rule(self.multiworld.get_entrance("9 Stars", self.player), lambda state: self.has_rarity_weapon(state, 7))

    def generate_output(self, output_directory: str) -> None:
        content = (
            f"Seed: {self.randomizer_seed}\n"
            "Settings: gYHAAIAAAAAAAAAAIA==:AABkAGQAYQA4AA==\n"
        )

        # We have to conform to the factorio naming scheme, otherwise the website is unhappy
        mod_name = f"AP-{self.multiworld.seed_name}-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}"
        mod_dir = os.path.join(output_directory, mod_name)
        container = MhwContainer(
            mod_dir,
            output_directory,
            self.player,
            self.multiworld.get_file_safe_player_name(self.player),
            content)
        container.write()

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict("death_link")
