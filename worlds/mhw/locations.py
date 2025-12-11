from BaseClasses import Location, LocationProgressType
from .game_id import mhw_name
from .locs.item_locations import common_items, break_items, common_high_rank_items, break_high_rank_items, gather_items, \
    gather_high_rank_items
from .locs.quest_locations import optional_quests, story_quests


class MhwLocation(Location):
    game = mhw_name

class MhwMainQuestLocation(MhwLocation):
    progress_type = LocationProgressType.PRIORITY

class MhwFillerLocation(MhwLocation):
    progress_type = LocationProgressType.EXCLUDED


from_common = {k: name for region_dict in common_items.values() for k, name in region_dict.items()}
from_common_high_rank = {k: name for region_dict in common_high_rank_items.values() for k, name in region_dict.items()}
from_break = {k: name for region_dict in break_items.values() for k, name in region_dict.items()}
from_break_high_rank = {k: name for region_dict in break_high_rank_items.values() for k, name in region_dict.items()}
from_story_quest = {k: name for region_dict in story_quests.values() for k, name in region_dict.items()}
from_quest = {k: name for region_dict in optional_quests.values() for k, name in region_dict.items()}
location_table = {
    **from_common,
    **from_common_high_rank,
    **from_break,
    **from_break_high_rank,
    **from_story_quest,
    **from_quest,
    **gather_items,
    **gather_high_rank_items,
}

location_name_groups = {
    "Common Items": {name for name in from_common.values()},
    "Break Items": {name for name in from_break.values()},
    "Common HR Items": {name for name in from_common_high_rank.values()},
    "Break HR Items": {name for name in from_break_high_rank.values()},
    "Story Quests": {name for name in from_story_quest.values()},
    "Optional Quests": {name for name in from_quest.values()},
    "Gather Items": {name for name in gather_items.values()},
    "Gather HR Items": {name for name in gather_high_rank_items.values()},
}