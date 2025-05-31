BG_COLOUR = "#021e42"
FG_COLOUR = "#a2bde0"
BIG_FONT = ("Times", 30, "bold")
NORM_FONT = ("Times", 15, "bold")
SMALL_FONT = ("Times", 10, "bold")
POSITION = "1200x658+150+150"
LIST_OF_LANGUAGES = ["English", "Chinese", "Malay", "Tamil", "Spanish", "French", "Tagalog", "German"]
HEAL = "50P - Increases your current HP by 50%."
AURA = "50P - Permanently lowers the enemy's DP by 50%."
TRICK = "90P - Acts as a force-field for all players. Lasts one round. The enemy's AP is inflicted onto themselves, \
their turn is skipped."
BOULDER_BRUTE = "75P - Combines the AP of both characters, inflicting 75% of that value onto the enemy."
CARBON_PROTECT = "80P - All players will be immune to any damage. Lasts one round. Enemy's turn is skipped."
PRESSURISE = "50P - Permanently increases your DP by 15%."
PRISMATIC_BEAM = "80P - Net Damage inflicted is 2x the Enemy's DP."
GLIMMER = "50P - Permanently increases your AP by 50%."
ILLUMINATE = "25P - Absorbs 10% of the Enemy's DP."
DICT_OF_CLASSES = {
    "Lux": { 
        "Prismatic Beam": PRISMATIC_BEAM,
        "Glimmer": GLIMMER,
        "Illuminate": ILLUMINATE,
    },
    "Psychic": { 
        "Heal": HEAL,
        "Aura": AURA,
        "Trick": TRICK,
    },
    "Mineral": { 
        "Boulder Brute": BOULDER_BRUTE,
        "Carbon Protect": CARBON_PROTECT,
        "Pressurise": PRESSURISE
    },
}

LIST_OF_SKILL_POINTS = [50, 50, 90, 75, 80, 50, 80, 50, 25]