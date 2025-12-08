from worlds.mhw.game_id import mhw_location_item_id


def get_id(base_id):
    return mhw_location_item_id + base_id


# Low Rank:
# Great Jagras, Kulu, Pukei-Pukei, Barroth, Jyuratodus, Tobi-Kadachi, Anjanath, Paolumu, Radobaan, Legiana, Odogaron, Rathalos, Diablos
# Optional: Tzitzi yaku, Great Girros, [Rathian?],

great_jagras = 7
kulu_ya_ku = 27
pukei = 24
barroth = 21
jyuratodus = 29
tobi_kadachi = 30
anjanath = 0

paolumu = 31
radobaan = 35
legiana = 32
odogaron = 34
rathalos = 1
diablos = 12
tzitzi_ya_ku = 28
great_girros = 33
rathian = 9
kirin = 14

common_items = {
    great_jagras: {
        get_id(302): "Great Jagras Scale",
        get_id(303): "Great Jagras Hide",
        get_id(305): "Great Jagras Claw"
    },
    kulu_ya_ku: {
        get_id(309): "Kulu-Ya-Ku Scale",
        get_id(310): "Kulu-Ya-Ku Hide",
        get_id(311): "Kulu-Ya-Ku Plume",
        get_id(312): "Kulu-Ya-Ku Scale",
    },
    pukei: {
        get_id(317): "Pukei-Pukei Scale",
        get_id(318): "Pukei-Pukei Shell",
        get_id(319): "Pukei-Pukei Quill",
        get_id(320): "Pukei-Pukei Sac",
        get_id(321): "Pukei-Pukei Tail",
    },
    barroth: {
        get_id(326): "Barroth Shell",
        get_id(327): "Barroth Ridge",
        get_id(328): "Barroth Claw",
        get_id(329): "Barroth Scalp",
        get_id(330): "Barroth Tail",
        get_id(331): "Fertile Mud",
    },
    jyuratodus: {
        get_id(335): "Jyuratodus Scale",
        get_id(336): "Jyuratodus Shell",
        get_id(337): "Jyuratodus Fang",
        get_id(338): "Jyuratodus Fin",
    },
    tobi_kadachi: {
        get_id(343): "Tobi-Kadachi Scale",
        get_id(344): "Tobi-Kadachi Pelt",
        get_id(345): "Tobi-Kadachi Membrane",
        get_id(346): "Tobi-Kadachi Claw",
        get_id(347): "Tobi-Kadachi Electrode",
    },
    anjanath: {
        get_id(352): "Anjanath Scale",
        get_id(353): "Anjanath Pelt",
        get_id(354): "Anjanath Fang",
        get_id(355): "Anjanath Nosebone",
    },
    rathian: {
        get_id(363): "Rathian Scale",
        get_id(364): "Rathian Shell",
        get_id(365): "Rathian Webbing",
    },
    tzitzi_ya_ku: {
        get_id(374): "Tzitzi-Ya-Ku Scale",
        get_id(375): "Tzitzi-Ya-Ku Hide",
        get_id(376): "Tzitzi-Ya-Ku Claw",
        get_id(377): "Tzitzi-Ya-Ku Photophore",
    },
    paolumu: {
        get_id(382): "Paolumu Pelt",
        get_id(383): "Paolumu Scale",
        get_id(384): "Paolumu Shell",
        get_id(385): "Paolumu Webbing",
    },
    great_girros: {
        get_id(390): "Great Girros Scale",
        get_id(391): "Great Girros Hide",
        get_id(392): "Great Girros Hood",
        get_id(393): "Great Girros Fang",
        get_id(394): "Great Girros Tail",
    },
    radobaan: {
      get_id(399): "Radoban Scale",
      get_id(400): "Radoban Shell",
      get_id(401): "Radoban Oilshell",
      get_id(402): "Wyvern Bonemass",
      get_id(404): "Radobaan Marrow",
    },
    legiana: {
        get_id(408): "Legiana Scale",
        get_id(409): "Legiana Hide",
        get_id(410): "Legiana Claw",
        get_id(411): "Legiana Webbing",
    },
    odogaron: {
        get_id(419): "Odogaron Scale",
        get_id(420): "Odogaron Sinew",
        get_id(421): "Odogaron Claw",
        get_id(422): "Odogaron Fang",
    },
    rathalos: {
        get_id(430): "Rathalos Scale",
        get_id(431): "Rathalos Shell",
        get_id(432): "Rathalos Webbing",
        get_id(434): "Rath Wingtalon",
        get_id(435): "Rathalos Marrow",
    },
    diablos: {
        get_id(446): "Diablos Shell",
        get_id(447): "Diablos Ridge",
        get_id(448): "Diablos Tailcase",
        get_id(449): "Diablos Fang",
        get_id(451): "Diablos Marrow",
        get_id(452): "Diablos Carapace",
    },
    kirin: {
        get_id(459): "Kirin Hide",
        get_id(460): "Kirin Tail",
        get_id(461): "Kirin Mane",
        get_id(462): "Kirin Thunderhorn",
    }
}

# Items that are usually only obtained after the player breaks a monster part or are very rare
break_items = {
    great_jagras: {
        get_id(304): "Great Jagras Mane (Break Head)"
    },
    anjanath: {
        get_id(356): "Anjanath Tail",
        get_id(357): "Anjanath Plate",
    },
    rathian: {
        get_id(366): "Rathian Spike",
        get_id(367): "Rathian Plate",
    },
    legiana: {
        get_id(412): "Legiana Tail Webbing",
        get_id(413): "Legiana Plate",
    },
    odogaron: {
        get_id(423): "Odogaron Tail",
        get_id(424): "Odogaron Plate",
    },
    rathalos: {
        get_id(433): "Rathalos Tail",
        get_id(436): "Rathalos Plate",
    },
    diablos: {
        get_id(450): "Twisted Horn",
    },
}
