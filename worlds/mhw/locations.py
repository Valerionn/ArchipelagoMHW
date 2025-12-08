from BaseClasses import Location, LocationProgressType
from .game_id import mhw_name
from .locs.item_locations import common_items, break_items
from .locs.quest_locations import optional_quests, story_quests


class MhwLocation(Location):
    game = mhw_name

class MhwMainQuestLocation(MhwLocation):
    progress_type = LocationProgressType.PRIORITY


from_common = {k: name for region_dict in common_items.values() for k, name in region_dict.items()}
from_break = {k: name for region_dict in break_items.values() for k, name in region_dict.items()}
from_story_quest = {k: name for region_dict in story_quests.values() for k, name in region_dict.items()}
from_quest = {k: name for region_dict in optional_quests.values() for k, name in region_dict.items()}
location_table = {
    **from_common,
    **from_break,
    **from_story_quest,
    **from_quest,
}

location_name_groups = {
    "Common Items": {name for name in from_common.values()},
    "Break Items": {name for name in from_break.values()},
    "Quest Items": {name for name in from_quest.values()},
}