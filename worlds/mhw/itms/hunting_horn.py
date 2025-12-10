from worlds.mhw.game_id import mhw_weapon_id

hunting_horn_weapon_category = 5


def get_id(base_id):
    return mhw_weapon_id + hunting_horn_weapon_category * 1000 + base_id

# https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Weapon-ID-Dump-(Longsword,-Hammer,-Hunting-Horn)
hunting_horns_by_rarity = {
    0: {
#        get_id(10): "Metal Bagpipe I",
        get_id(11): "Metal Bagpipe II",
        get_id(45): "Bone Horn I",
        get_id(46): "Bone Horn II",
    },
    1: {
        get_id(12): "Metal Bagpipe III",
        get_id(25): "Kulu Duda I",
        get_id(35): "Aqua Bagpipe I",
        get_id(47): "Bone Horn III",
        get_id(60): "Blooming Horn I",
        get_id(73): "Sonic Horn I",
    },
    2: {
        get_id(13): "Great Bagpipe I",
        get_id(20): "Thunder Gaida I",
        get_id(25): "Kulu Duda II",
        get_id(31): "Valkyrie Chordmaker",
        get_id(36): "Aqua Bagpipe II",
        get_id(48): "Hard Bone Horn I",
        get_id(55): "Blazing Horn I",
        get_id(61): "Blooming Horn II",
        get_id(66): "Lumu Horn I",
        get_id(74): "Sonic Horn II",
        get_id(79): "Spiked Horn I",
        get_id(84): "Dragonbone Auldhorn I",
    },
    3: {
        get_id(14): "Great Bagpipe II",
        get_id(21): "Thunder Gaida II",
        get_id(27): "Kulu Duda III",
        get_id(37): "Aqua Bagpipe III",
        get_id(41): "Glacial Bagpipe I",
        get_id(49): "Hard Bone Horn II",
        get_id(56): "Blazing Horn II",
        get_id(62): "Blooming Horn III",
        get_id(67): "Lumu Horn II",
        get_id(75): "Sonic Horn III",
        get_id(80): "Spiked Horn II",
        get_id(85): "Dragonbone Auldhorn II",
        get_id(87): "Thundercry Horn",
    }
}
