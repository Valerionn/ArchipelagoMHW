import typing

from BaseClasses import Region
from .game_id import mhw_location_quest_id
from .locations import MhwLocation, MhwMainQuestLocation
from .locs.item_locations import common_items, break_items
from .locs.quest_locations import optional_quests, story_quests
from .monster_randomizer import MonsterRandomizer, low_rank_monsters
from .xorshift128 import XorShift128Generator

if typing.TYPE_CHECKING:
    from . import MhwWorld


def add_locations_for_monster(region: Region, monster_id: int):
    region.add_locations({name: k for k, name in common_items[monster_id].items()}, MhwLocation)
    if monster_id in break_items:
        region.add_locations({name: k for k, name in break_items[monster_id].items()}, MhwLocation)


def add_monster_to_location(region: Region, monster_id: int, monsters_added: set[int]):
    if monster_id in monsters_added:
        return
    monsters_added.add(monster_id)
    add_locations_for_monster(region, monster_id)


def create_regions(world: "MhwWorld"):
    player = world.player
    multiworld = world.multiworld

    monster_randomizer = MonsterRandomizer(XorShift128Generator(world.randomizer_seed))

    random_monsters_by_quest = monster_randomizer.get_random_monsters_by_quest()
    monsters_added = set()

    # Start with Menu Region
    menu = Region("Menu", player, multiworld)
    multiworld.regions.append(menu)

    # One Star
    one_star = Region("One Star", player, multiworld)
    one_star.add_locations({name: k for k, name in story_quests[1].items()}, MhwMainQuestLocation)
    for quest_id in story_quests[1].keys():
        add_monster_to_location(one_star, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    menu.connect(one_star)

    # Two Stars
    two_stars = Region("Two Stars", player, multiworld)
    two_stars.add_locations({name: k for k, name in story_quests[2].items()}, MhwMainQuestLocation)
    two_stars.add_locations({name: k for k, name in optional_quests[2].items()}, MhwLocation)
    for quest_id in story_quests[2].keys():
        add_monster_to_location(two_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    one_star.connect(two_stars, "Two Stars")

    # Three Stars
    three_stars = Region("Three Stars", player, multiworld)
    three_stars.add_locations({name: k for k, name in story_quests[3].items()}, MhwMainQuestLocation)
    three_stars.add_locations({name: k for k, name in optional_quests[3].items()}, MhwLocation)
    for quest_id in story_quests[3].keys():
        add_monster_to_location(three_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    two_stars.connect(three_stars, "Three Stars")

    # Four Stars
    four_stars = Region("Four Stars", player, multiworld)
    four_stars.add_locations({name: k for k, name in story_quests[4].items()}, MhwMainQuestLocation)
    four_stars.add_locations({name: k for k, name in optional_quests[4].items()}, MhwLocation)
    for quest_id in story_quests[4].keys():
        add_monster_to_location(four_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    three_stars.connect(four_stars, "Four Stars")

    # Five Stars
    five_stars = Region("Five Stars", player, multiworld)
    five_stars.add_locations({name: k for k, name in story_quests[5].items()}, MhwMainQuestLocation)
    five_stars.add_locations({name: k for k, name in optional_quests[5].items()}, MhwLocation)
    for quest_id in story_quests[5].keys():
        add_monster_to_location(five_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)

    for monster_id in low_rank_monsters:
        if monster_id not in monsters_added:
            add_monster_to_location(five_stars, monster_id, monsters_added)
    four_stars.connect(five_stars, "Five Stars")

    # Victory
    multiworld.completion_condition[player] = lambda state: state.can_reach(five_stars, "Region", player)
