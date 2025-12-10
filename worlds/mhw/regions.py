import typing

from BaseClasses import Region
from .game_id import mhw_location_quest_id
from .locations import MhwLocation, MhwMainQuestLocation, MhwFillerLocation
from .locs.item_locations import common_items, break_items, common_high_rank_items, break_high_rank_items, gather_items, \
    gather_high_rank_items
from .locs.quest_locations import optional_quests, story_quests
from .monster_randomizer import MonsterRandomizer, low_rank_monsters, high_rank_monsters
from .xorshift128 import XorShift128Generator

if typing.TYPE_CHECKING:
    from . import MhwWorld


def add_locations_for_monster(region: Region, monster_id: int):
    region.add_locations({name: k for k, name in common_items[monster_id].items()}, MhwLocation)
    if monster_id in break_items:
        region.add_locations({name: k for k, name in break_items[monster_id].items()}, MhwFillerLocation)


def add_monster_to_location(region: Region, monster_id: int, monsters_added: set[int]):
    if monster_id in monsters_added:
        return
    monsters_added.add(monster_id)
    add_locations_for_monster(region, monster_id)


def add_locations_for_hr_monster(region: Region, monster_id: int):
    region.add_locations({name: k for k, name in common_high_rank_items[monster_id].items()}, MhwLocation)
    if monster_id in break_high_rank_items:
        region.add_locations({name: k for k, name in break_high_rank_items[monster_id].items()}, MhwFillerLocation)


def add_hr_monster_to_location(region: Region, monster_id: int, hr_monsters_added: set[int]):
    if monster_id in hr_monsters_added:
        return
    hr_monsters_added.add(monster_id)
    add_locations_for_hr_monster(region, monster_id)


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
    one_star = Region("1 Star", player, multiworld)
    one_star.add_locations({name: k for k, name in story_quests[1].items()}, MhwMainQuestLocation)
    for quest_id in story_quests[1].keys():
        add_monster_to_location(one_star, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    menu.connect(one_star)

    # Two Stars
    two_stars = Region("2 Stars", player, multiworld)
    two_stars.add_locations({name: k for k, name in story_quests[2].items()}, MhwMainQuestLocation)
    two_stars.add_locations({name: k for k, name in optional_quests[2].items()}, MhwLocation)
    for quest_id in story_quests[2].keys():
        add_monster_to_location(two_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    one_star.connect(two_stars, "2 Stars")

    # Three Stars
    three_stars = Region("3 Stars", player, multiworld)
    three_stars.add_locations({name: k for k, name in story_quests[3].items()}, MhwMainQuestLocation)
    three_stars.add_locations({name: k for k, name in optional_quests[3].items()}, MhwLocation)
    for quest_id in story_quests[3].keys():
        add_monster_to_location(three_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    two_stars.connect(three_stars, "3 Stars")

    # Four Stars
    four_stars = Region("4 Stars", player, multiworld)
    four_stars.add_locations({name: k for k, name in story_quests[4].items()}, MhwMainQuestLocation)
    four_stars.add_locations({name: k for k, name in optional_quests[4].items()}, MhwLocation)
    for quest_id in story_quests[4].keys():
        add_monster_to_location(four_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    three_stars.connect(four_stars, "4 Stars")

    # Five Stars
    five_stars = Region("5 Stars", player, multiworld)
    five_stars.add_locations({name: k for k, name in story_quests[5].items()}, MhwMainQuestLocation)
    five_stars.add_locations({name: k for k, name in optional_quests[5].items()}, MhwLocation)
    for quest_id in story_quests[5].keys():
        add_monster_to_location(five_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)

    # Additional low rank monsters that haven't been added yet
    for monster_id in low_rank_monsters:
        if monster_id not in monsters_added:
            add_monster_to_location(five_stars, monster_id, monsters_added)

    # Gather items are only filler, but we still only consider them all reachable once we have finished low rank (and all regions are available)
    five_stars.add_locations({name: k for k, name in gather_items.items()}, MhwFillerLocation)

    four_stars.connect(five_stars, "5 Stars")

    # High Rank
    monsters_added = set()

    # Six stars
    six_stars = Region("6 Stars", player, multiworld)
    six_stars.add_locations({name: k for k, name in story_quests[6].items()}, MhwMainQuestLocation)
    six_stars.add_locations({name: k for k, name in optional_quests[6].items()}, MhwLocation)
    for quest_id in story_quests[6].keys():
        add_hr_monster_to_location(six_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    five_stars.connect(six_stars, "6 Stars")

    # Seven stars
    seven_stars = Region("7 Stars", player, multiworld)
    seven_stars.add_locations({name: k for k, name in story_quests[7].items()}, MhwMainQuestLocation)
    seven_stars.add_locations({name: k for k, name in optional_quests[7].items()}, MhwLocation)
    for quest_id in story_quests[7].keys():
        add_hr_monster_to_location(seven_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    six_stars.connect(seven_stars, "7 Stars")

    # Eight stars
    eight_stars = Region("8 Stars", player, multiworld)
    eight_stars.add_locations({name: k for k, name in story_quests[8].items()}, MhwMainQuestLocation)
    eight_stars.add_locations({name: k for k, name in optional_quests[8].items()}, MhwLocation)
    for quest_id in story_quests[8].keys():
        add_hr_monster_to_location(eight_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    seven_stars.connect(eight_stars, "8 Stars")

    # Nine stars
    nine_stars = Region("9 Stars", player, multiworld)
    nine_stars.add_locations({name: k for k, name in story_quests[9].items()}, MhwMainQuestLocation)
    nine_stars.add_locations({name: k for k, name in optional_quests[9].items()}, MhwLocation)
    for quest_id in story_quests[9].keys():
        add_hr_monster_to_location(nine_stars, random_monsters_by_quest[quest_id - mhw_location_quest_id], monsters_added)
    eight_stars.connect(nine_stars, "9 Stars")

    # Additional high rank monsters that haven't been added yet
    for monster_id in high_rank_monsters:
        if monster_id not in monsters_added:
            add_hr_monster_to_location(nine_stars, monster_id, monsters_added)

    # Gather items are only filler, but we still only consider them all reachable once we have finished high rank (and all regions are available)
    nine_stars.add_locations({name: k for k, name in gather_high_rank_items.items()}, MhwFillerLocation)

    # Victory
    multiworld.completion_condition[player] = lambda state: state.can_reach(nine_stars, "Region", player)
