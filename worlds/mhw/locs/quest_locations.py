from worlds.mhw.game_id import mhw_location_quest_id


def get_id(base_id):
    return mhw_location_quest_id + base_id


story_quests = {
    1: {
        get_id(102): "A Kestodon Kerfuffle",
        get_id(103): "The Great Jagras Hunt",
    },
    2: {
        get_id(201): "Bird-Brained Bandit",
        get_id(205): "Urgent: Pukei-Pukei Hunt",
        get_id(301): "The Best Kind of Quest",
        get_id(302): "Sinister Shadows in the Swamp",
    },
    3: {
        get_id(305): "Flying Sparks: Tobi-Kadachi",
        get_id(306): "The Encroaching Anjanath",
    },
    4: {
        get_id(401): "One for the History Books",
        get_id(405): "Ballooning Problems",
        get_id(407): "Radobaan Roadblock",
        get_id(408): "Legiana: Embodiment of Elegance",
    },
    5: {
        get_id(501): "Into the Bowels of the Vale",
        get_id(502): "A Fiery Throne Atop the Forest",
        get_id(503): "Horned Tyrant Below the Sands",
        # This is technically 6*, but it's also the end of Low Rank, and only rarity 4 stuff is available
        get_id(504): "A Colossal Task",
    },
    6: {
        get_id(601): "Invader in the Waste",
        get_id(605): "Tickled Pink",
    },
    7: {
        get_id(607): "Old World Monster in the New World",
    },
    8: {
        get_id(701): "A Wound and a Thirst",
        get_id(801): "Kushala Daora, Dragon of Steel",
        get_id(802): "Teostra the Infernal",
        get_id(803): "Hellish Fiend Vaal Hazak",
    },
    9: {
        get_id(804): "Land of Convergence",
    },
}

optional_quests = {
    2: {
        get_id(251): "The Great Glutton",
        get_id(252): "Camp Crasher",
    },
    3: {
        get_id(351): "Scatternut Shortage",
        get_id(352): "The Current Situation",
        get_id(361): "Mired in the Spire",
        get_id(362): "The Piscine Problem",
    },
    4: {
        get_id(451): "One Helluva Sinus Infection",
        get_id(461): "Royal Relocation",
        get_id(472): "A Tzitzi for Science",
        get_id(472): "Sorry You're Not Invited",
        get_id(482): "A Rotten Thing To Do",
        get_id(483): "A Bone to Pick",
    },
    5: {
        get_id(501): "When Desire Becomes an Obsession",
        get_id(561): "Twin Spires Upon the Sands",
        get_id(571): "A Humid Headache",
        get_id(581): "Scratching the Itch",
    },
    6: {
        get_id(651): "Hard to Swallow",
        get_id(652): "Googly-eyed Green Monster",
        get_id(653): "A Hair-Raising Experience",
        get_id(654): "It Can't See You if You Don't Move",
        get_id(655): "The Sleeping Sylvan Queen",
        get_id(655): "The Sleeping Sylvan Queen",
        get_id(661): "Keep Your Hands to Yourself!",
        get_id(661): "Keep Your Hands to Yourself!",
        get_id(662): "A Crown of Mud and Anger",
        get_id(663): "Pukei-Pukei Ambush",
        get_id(665): "Up to Your Waist in the Waste",
        get_id(666): "Brown Desert, Green Queen",
        get_id(667): "Trespassing Troublemaker",
        get_id(671): "Say Cheese!",
        get_id(672): "Loop the Paolumu",
        get_id(681): "A Tingling Taste",
        get_id(682): "Stuck in a Rut",
        get_id(693): "Dodogama Drama",
    },
    7: {
        get_id(751): "Rathalos Rematch",
        get_id(752): "Rathalos in Blue",
        get_id(761): "Pretty In Pink",
        get_id(762): "Well, That Diablos!",
        get_id(763): "Two-horned Hostility",
        get_id(771): "A Cherry Wind upon the Reefs",
        get_id(772): "Legiana: Highlands Royalty",
        get_id(781): "Odogaron Unleashed",
        get_id(791): "Lavasioth, Monster of Magma",
        get_id(792): "Ore-eating Occupier",
        get_id(793): "Ruler of the Azure Skies",
        get_id(793): "Ruler of the Azure Skies",
    },
    8: {
        get_id(881): "Stirrings from the Grave",
        # This quest is doubled, so ignore it for now
        # get_id(891): "The Eater of Elders",
        # get_id(892): "Master of the Gale",
        # Doubled with 896
        # get_id(893): "Hellfire's Stronghold",
        # get_id(894): "The Eater of Elders",
        # get_id(895): "The Winds of Wrath Bite Deep",
        #get_id(896): "The Fires of Hell Bite Deep",
    },
    9: {
        get_id(961): "Beyond the Blasting Scales",
        get_id(971): "Thunderous Rumble in the Highlands",
    }
}
