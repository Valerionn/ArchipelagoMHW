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

# High Rank+
pink_rathian = 10
azure_rathalos = 11
black_diablos = 13
dodogama = 37
lavasioth = 19
uragaan = 22
bazelgeuse = 39
nergigante = 25
vaal_hazak = 36
teostra = 18
kushala_daora = 16
deviljho = 20
lunastra = 17

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
        get_id(312): "Kulu-Ya-Ku Beak",
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
        get_id(304): "Great Jagras Mane"
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

common_high_rank_items = {
    great_jagras: {
        get_id(306): "Great Jagras Scale+",
        get_id(307): "Great Jagras Hide+",
        get_id(308): "Great Jagras Claw+",
    },
    kulu_ya_ku: {
        get_id(313): "Kulu-Ya-Ku Scale+",
        get_id(314): "Kulu-Ya-Ku Hide+",
        get_id(315): "Kulu-Ya-Ku Plume+",
        get_id(316): "Kulu-Ya-Ku Beak+",
    },
    pukei: {
        get_id(322): "Pukei-Pukei Scale+",
        get_id(323): "Pukei-Pukei Carapace",
        get_id(324): "Pukei-Pukei Wing",
        get_id(325): "Pukei-Pukei Sac+",
    },
    barroth: {
        get_id(332): "Barroth Carapace",
        get_id(333): "Barroth Ridge+",
        get_id(334): "Barroth Claw+",
    },
    jyuratodus: {
        get_id(339): "Jyuratodus Scale+",
        get_id(340): "Jyuratodus Carapace",
        get_id(341): "Jyuratodus Fang+",
        get_id(342): "Jyuratodus Fin++",
    },
    tobi_kadachi: {
        get_id(348): "Tobi-Kadachi Scale+",
        get_id(349): "Tobi-Kadachi Pelt+",
        get_id(350): "Tobi-Kadachi Claw+",
        get_id(351): "Tobi-Kadachi Electrode+",
    },
    anjanath: {
        get_id(358): "Anjanath Scale+",
        get_id(359): "Anjanath Pelt+",
        get_id(360): "Anjanath Fang+",
        get_id(360): "Anjanath Nosebone+",
    },
    rathian: {
        get_id(368): "Rathian Scale+",
        get_id(369): "Rathian Carapace",
        get_id(370): "Rathian Spike+",
    },
    pink_rathian: {
        get_id(372): "Pink Rathian Scale+",
        get_id(373): "Pink Rathian Carapace",
    },
    tzitzi_ya_ku: {
        get_id(378): "Tzitzi-Ya-Ku Scale+",
        get_id(379): "Tzitzi-Ya-Ku Hide+",
        get_id(380): "Tzitzi-Ya-Ku Claw+",
        get_id(381): "Tzitzi-Ya-Ku Photophore+",
    },
    paolumu: {
        get_id(386): "Paolumu Pelt+",
        get_id(387): "Paolumu Scale+",
        get_id(388): "Paolumu Carapace+",
        get_id(389): "Paolumu Wing",
    },
    great_girros: {
        get_id(395): "Great Girros Scale+",
        get_id(396): "Great Girros Hide+",
        get_id(397): "Great Girros Hood+",
        get_id(398): "Great Girros Fang+",
    },
    radobaan: {
        get_id(405): "Radobaan Scale+",
        get_id(406): "Radobaan Carapace",
        get_id(407): "Radobaan Medulla",
    },
    legiana: {
        get_id(414): "Legiana Scale+",
        get_id(415): "Legiana Hide+",
        get_id(416): "Legiana Claw+",
        get_id(417): "Legiana Wing",
    },
    odogaron: {
        get_id(425): "Odogaron Scale+",
        get_id(426): "Odogaron Sinew+",
        get_id(427): "Odogaron Claw+",
        get_id(428): "Odogaron Fang+",
    },
    rathalos: {
        get_id(437): "Rathalos Scale+",
        get_id(438): "Rathalos Carapace",
        get_id(439): "Rathalos Wing",
        get_id(440): "Rathalos Medulla",
    },
    azure_rathalos: {
        get_id(442): "Azure Rathalos Scale+",
        get_id(443): "Azure Rathalos Carapace",
        get_id(445): "Azure Rathalos Wing",
    },
    diablos: {
        get_id(452): "Diablos Carapace",
        get_id(453): "Diablos Ridge+",
        get_id(455): "Blos Medulla",
    },
    black_diablos: {
        get_id(456): "Black Diablos Carapace",
        get_id(457): "Black Diablos Ridge+",
    },
    kirin: {
        get_id(463): "Kirin Hide+",
        get_id(464): "Kirin Thundertail",
        get_id(465): "Kirin Azure Horn",
    },
    dodogama: {
        get_id(474): "Dodogama Scale+",
        get_id(475): "Dodogama Hide+",
        get_id(476): "Dodogama Jaw",
        get_id(477): "Dodogama Talon",
        get_id(478): "Dodogama Tail",
    },
    lavasioth: {
        get_id(479): "Lavasioth Scale+",
        get_id(480): "Lavasioth Carapace",
        get_id(481): "Lavasioth Fang+",
        get_id(482): "Lavasioth Fin+",
    },
    uragaan: {
        get_id(483): "Uragaan Scale+",
        get_id(484): "Uragaan Carapace",
        get_id(485): "Uragaan Jaw",
        get_id(486): "Uragaan Scute",
        get_id(487): "Uragaan Marrow",
    },
    bazelgeuse: {
        get_id(490): "Bazelgeuse Scale+",
        get_id(491): "Bazelgeuse Carapace",
        get_id(493): "Bazelgeuse Fuse",
        get_id(494): "Bazelgeuse Talon",
        get_id(495): "Bazelgeuse Wing",
    },
    nergigante: {
        get_id(497): "Immortal Dragonscale",
        get_id(498): "Nergigante Carapace",
        get_id(502): "Nergigante Talon",
        get_id(503): "Nergigante Regrowth Plate",
    },
    vaal_hazak: {
        get_id(505): "Deceased Scale",
        get_id(506): "Vaal Hazak Carapace",
        get_id(510): "Vaal Hazak Talon",
        get_id(511): "Vaal Hazak Wing",
    },
    teostra: {
        get_id(514): "Teostra Carapace",
        get_id(515): "Teostra Mane",
        get_id(517): "Teostra Horn+",
        get_id(518): "Fire Dragon Scale+",
        get_id(519): "Teostra Claw+",
    },
    kushala_daora: {
        get_id(523): "Daora Carapace",
        get_id(524): "Daora Dragon Scale+",
        get_id(525): "Daora Webbing",
        get_id(528): "Daora Claw+",
    },
    deviljho: {
        get_id(879): "Deviljho Scale",
        get_id(880): "Deviljho Hide",
        get_id(881): "Deviljho Tallfang",
        get_id(882): "Deviljho Talon",
    },
    lunastra: {
        get_id(895): "Lunastra Scale+",
        get_id(899): "Lunastra Mane",
    }
}

break_high_rank_items = {
    anjanath: {
        get_id(362): "Anjanath Gem",
    },
    rathian: {
        get_id(371): "Rathian Ruby",
    },
    legiana: {
        get_id(418): "Legiana Gem",
    },
    odogaron: {
        get_id(429): "Odogaron Gem",
    },
    rathalos: {
        get_id(441): "Rathalos Ruby",
    },
    azure_rathalos: {
        get_id(444): "Azure Rathalos Tail",
    },
    diablos: {
        get_id(454): "Majestic Horn",
    },
    black_diablos: {
        get_id(458): "Black Spiral Horn+",
    },
    uragaan: {
        get_id(488): "Uragaan Ruby",
        get_id(489): "Lava Nugget",
    },
    bazelgeuse: {
        get_id(492): "Bazelgeuse Tail",
        get_id(496): "Bazelgeuse Gem",
    },
    nergigante: {
        get_id(500): "Nergigante Tail",
        get_id(501): "Nergigante Horn+",
        get_id(504): "Nergigante Gem",
    },
    vaal_hazak: {
        get_id(507): "Vaal Hazak Membrane",
        get_id(508): "Vaal Hazak Tail",
        get_id(509): "Vaal Hazak Fang+",
        get_id(513): "Vaal Hazak Gem",
    },
    teostra: {
        get_id(516): "Teostra Tail",
        get_id(520): "Teostra Webbing",
        get_id(521): "Teostra Powder",
        get_id(522): "Teostra Gem",
    },
    kushala_daora: {
        get_id(526): "Daora Horn+",
        get_id(527): "Daora Tail",
        get_id(529): "Daora Gem",
    },
    deviljho: {
        get_id(883): "Deviljho Scalp",
        get_id(884): "Deviljho Tail",
        get_id(885): "Deviljho Saliva",
        get_id(886): "Deviljho Gem",
    },
    lunastra: {
        get_id(896): "Lunastra Wing",
        get_id(897): "Lunastra Gem",
        get_id(898): "Lunastra Carapace",
        get_id(900): "Lunastra Tail",
        get_id(901): "Lunastra Horn",
    }
}

gather_items = {
    get_id(205): "Iron Ore",
    get_id(206): "Machalite Ore",
    get_id(207): "Dragonite Ore",
    get_id(210): "Earth Crystal",
    get_id(211): "Coral Crystal",
    get_id(213): "Lightcrystal",
    get_id(216): "Aquacore Ore",
    get_id(225): "Sturdy Bone",
    get_id(227): "Ancient Bone",
    get_id(228): "Boulder Bone",
    get_id(229): "Coral Bone",
    get_id(230): "Warped Bone",
    get_id(236): "Monster Bone S",
}

gather_high_rank_items = {
    get_id(208): "Carbalite Ore",
    get_id(209): "Fucium Ore",
    get_id(212): "Dragonvein Crystal",
    get_id(214): "Novacrystal",
    get_id(215): "Firecell Stone",
    get_id(217): "Spiritcore Ore",
    get_id(218): "Dreamcore Ore",
    get_id(219): "Dragoncore Ore",
    get_id(226): "Quality Bone",
    get_id(231): "Brutal Bone",
    get_id(232): "Dragonbone Relic",
    get_id(233): "Unknown Skull",
}
