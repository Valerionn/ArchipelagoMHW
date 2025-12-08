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
        get_id(504): "A Colossal Task",
    }
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
    }
}