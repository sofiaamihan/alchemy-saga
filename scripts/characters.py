from scripts.constants import *
from scripts.functions import *
from scripts.variables import *
from scripts.photos import *

class Characters:
    def __init__(self, job_class, name, hp, ap, dp, mp, sp, image, skills):
        self.job_class = job_class
        self.name = name
        self.hp = hp
        self.ap = ap
        self.dp = dp
        self.mp = mp
        self.SP = sp
        self.HP = hp
        self.AP = ap
        self.DP = dp
        self.MP = mp
        self.image = image
        self.skills = skills

    def display_stats(self):
        return f'''
-----{self.name}-----
JOB CLASS: {self.job_class}
HP: {self.hp}
AP: {self.ap}
DP: {self.dp}
MP: {self.mp}
SP: {self.SP}
'''

    def restart(self):
        self.hp = self.HP
        self.ap = self.AP
        self.dp = self.DP
        self.mp = self.MP

    def heal(self):
        self.hp /= 0.5
        self.hp = int(self.hp)
        self.mp -= LIST_OF_SKILL_POINTS[0]
        insert_text("\nYou used Heal! Health is restored.", content)

    def aura(self, enemy):
        enemy.dp /= 2
        enemy.dp = int(enemy.dp)
        self.mp -= LIST_OF_SKILL_POINTS[1]
        insert_text("\nYou used Aura! Enemy's defence is lowered by 50%.", content)

    def trick(self, enemy):
        global net_attack, turns
        net_attack = enemy.ap - enemy.dp
        turns += 1
        self.mp -= LIST_OF_SKILL_POINTS[2]
        insert_text("\nYou used Trick! Force-field is up. Enemy skips a turn.", content)

    def boulder_brute(self, enemy):
        global net_attack
        net_attack = (self.ap + enemy.ap) * 0.75 - enemy.dp
        self.mp -= LIST_OF_SKILL_POINTS[3]
        insert_text("\nYou used Boulder Brute! Massive damage inflicted!", content)

    def carbon_protect(self):
        global turns
        self.mp -= LIST_OF_SKILL_POINTS[4]
        turns += 1
        insert_text("\nYou used Carbon Protect! Temporary immunity is activated. The enemy skips a turn.", content)

    def pressurise(self):
        self.dp *= 1.15
        self.dp = int(self.dp)
        self.mp -= LIST_OF_SKILL_POINTS[5]
        insert_text("\nYou used Pressurize! Defence is up.", content)

    def prismatic_beam(self, enemy):
        global net_attack
        net_attack = enemy.dp * 2
        self.mp -= LIST_OF_SKILL_POINTS[6]
        insert_text("\nYou used Astral Ray! Massive damage inflicted!", content)

    def glimmer(self):
        self.ap *= 1.5
        self.ap = int(self.ap)
        self.mp -= LIST_OF_SKILL_POINTS[7]
        insert_text("\nYou used Glimmer! Attack stats increased.", content)

    def illuminate(self, enemy):
        enemy.dp *= 0.9
        enemy.dp = int(enemy.dp)
        self.mp -= LIST_OF_SKILL_POINTS[8]
        insert_text("\nYou used Illuminate! Enemy's defence is lowered by 10%.", content)

isla = Characters(
    job_class="Psychic",
    name="Isla",
    hp=160,
    ap=108,
    dp=30,
    mp=150,
    sp=155,
    image=mod2_photo2,
    skills="Heal, Aura, Trick"
)
rosa = Characters(
    job_class="Mineral",
    name="Rosa",
    hp=180,
    ap=79,
    dp=49,
    mp=130,
    sp=82,
    image=mod2_photo3,
    skills="Boulder Brute, Carbon Protect, Pressurize"
)
jess = Characters(
    job_class="Lux",
    name="Jess",
    hp=140,
    ap=85,
    dp=28,
    mp=105,
    sp=178,
    image=mod2_photo4,
    skills="Astral Ray, Glimmer, Illuminate"
)
violet = Characters(
    job_class="Psychic",
    name="Violet",
    hp=170,
    ap=107,
    dp=36,
    mp=0,
    sp=167,
    image=mod2_photo5,
    skills=None
)
merida = Characters(
    job_class="Mineral",
    name="Merida",
    hp=190,
    ap=77,
    dp=45,
    mp=0,
    sp=79,
    image=mod2_photo6,
    skills=None
)
diego = Characters(
    job_class="Lux",
    name="Diego",
    hp=150,
    ap=89,
    dp=32,
    mp=0,
    sp=181,
    image=mod2_photo7,
    skills=None
)
LIST_OF_CHARACTERS = [isla, rosa, jess, violet, merida, diego]