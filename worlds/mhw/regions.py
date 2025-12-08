import typing

from BaseClasses import Region
from .locations import MhwLocation, MhwMainQuestLocation
from .locs.item_locations import common_items, break_items, great_jagras, legiana, pukei, jyuratodus, tzitzi_ya_ku, \
    rathalos, paolumu, tobi_kadachi, kulu_ya_ku, kirin, rathian, anjanath, radobaan
from .locs.quest_locations import optional_quests, story_quests

if typing.TYPE_CHECKING:
    from . import MhwWorld

def add_locations_for_monster(region: Region, monster_id: int):
    region.add_locations({name: k for k, name in common_items[monster_id].items()}, MhwLocation)
    if monster_id in break_items:
        region.add_locations({name: k for k, name in break_items[monster_id].items()}, MhwLocation)


def create_regions(world: "MhwWorld"):
    player = world.player
    multiworld = world.multiworld

    # Start with Menu Region
    menu = Region("Menu", player, multiworld)
    multiworld.regions.append(menu)

    # One Star
    one_star = Region("One Star", player, multiworld)
    one_star.add_locations({name: k for k, name in story_quests[1].items()}, MhwMainQuestLocation)
    add_locations_for_monster(one_star, legiana)
    menu.connect(one_star)

    # Two Stars
    two_stars = Region("Two Stars", player, multiworld)
    two_stars.add_locations({name: k for k, name in story_quests[2].items()}, MhwMainQuestLocation)
    two_stars.add_locations({name: k for k, name in optional_quests[2].items()}, MhwLocation)
    add_locations_for_monster(two_stars, pukei)
    add_locations_for_monster(two_stars, great_jagras)
    add_locations_for_monster(two_stars, tzitzi_ya_ku)
    add_locations_for_monster(two_stars, jyuratodus)
    one_star.connect(two_stars, "Two Stars")

    # Three Stars
    three_stars = Region("Three Stars", player, multiworld)
    three_stars.add_locations({name: k for k, name in story_quests[3].items()}, MhwMainQuestLocation)
    three_stars.add_locations({name: k for k, name in optional_quests[3].items()}, MhwLocation)
    add_locations_for_monster(three_stars, rathalos)
    add_locations_for_monster(three_stars, paolumu)
    two_stars.connect(three_stars, "Three Stars")

    # Four Stars
    four_stars = Region("Four Stars", player, multiworld)
    four_stars.add_locations({name: k for k, name in story_quests[4].items()}, MhwMainQuestLocation)
    four_stars.add_locations({name: k for k, name in optional_quests[4].items()}, MhwLocation)
    add_locations_for_monster(four_stars, tobi_kadachi)
    add_locations_for_monster(four_stars, kulu_ya_ku)
    add_locations_for_monster(four_stars, kirin)
    three_stars.connect(four_stars, "Four Stars")

    # Five Stars
    five_stars = Region("Five Stars", player, multiworld)
    five_stars.add_locations({name: k for k, name in story_quests[5].items()}, MhwMainQuestLocation)
    five_stars.add_locations({name: k for k, name in optional_quests[5].items()}, MhwLocation)
    add_locations_for_monster(five_stars, rathian)
    add_locations_for_monster(five_stars, anjanath)
    four_stars.connect(five_stars, "Five Stars")

    # Victory
    multiworld.completion_condition[player] = lambda state: state.can_reach(five_stars, "Region", player)
