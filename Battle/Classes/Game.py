import random
import math




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, magic, items, NAME):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['attack', 'magic', 'item']
        self.items = items
        self.name = NAME

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        if self.hp > self.maxhp:
            self.hp = self.maxhp

        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp = self.mp - cost
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        print(self.name+":")
        i = 1
        for item in self.actions:
            print("    ",str(i), " : ", item)
            i = i + 1

    def choose_magic(self):
        i = 1
        print("magic")
        for spell in self.magic:
            print(str(i) + " : ", spell.name, 'cost', str(spell.cost))
            i = i + 1

    def choose_item(self):
        i = 1
        print("Item")
        for item in self.items:
            print(str(i) + " : ", item["item"].name, "  ", item["item"].description, 'prop', str(item["item"].prop),
                  " x", str(item["quantity"]))
            i = i + 1

    def get_stats(self):
        i = 8 - len(self.name)
        alignment_string = i * " "
        j=2-math.floor(math.log10(self.hp))
        hp_align_str=j*" "
        maxj=2-math.floor(math.log10(self.maxhp))
        maxhp_align_str=maxj*" "
        j = 1 - math.floor(math.log10(self.mp))
        mp_align_str = j * " "
        maxj = 1 - math.floor(math.log10(self.maxmp))
        maxmp_align_str = j * " "
        hp_line=math.floor(30*self.hp/self.maxhp)
        mp_line=math.floor(10*self.mp/self.maxmp)
        print(
            bcolors.BOLD + "NAME         " + bcolors.OKGREEN + "    HP                                  " + bcolors.OKBLUE + "   MP")
        print(
            bcolors.OKGREEN + "                  ______________________________" + bcolors.OKBLUE + "         __________" + bcolors.ENDC)
        print(
            bcolors.BOLD + self.name + alignment_string + bcolors.OKGREEN + hp_align_str+str(
                self.hp) + "/"+str(self.maxhp)+maxhp_align_str+"  |"+hp_line*"▓"+(30-hp_line)*" "+"|" + bcolors.OKBLUE + " "+mp_align_str+str(self.mp)+"/"+str(self.maxmp)+maxmp_align_str+" |"+mp_line*"▓"+(10-mp_line)*" "+"|" + bcolors.ENDC)

    def get_enemy_stats(self):
        i = 8 - len(self.name)
        alignment_string = i * " "
        j=2-math.floor(math.log10(self.hp))
        hp_align_str=j*" "
        maxj=2-math.floor(math.log10(self.maxhp))
        maxhp_align_str=maxj*" "
        j = 1 - math.floor(math.log10(self.mp))
        mp_align_str = j * " "
        maxj = 1 - math.floor(math.log10(self.maxmp))
        maxmp_align_str = j * " "
        hp_line=math.floor(30*self.hp/self.maxhp)
        mp_line=math.floor(10*self.mp/self.maxmp)
        print(
            bcolors.BOLD + "NAME         " + bcolors.FAIL + "    HP                                  " + bcolors.OKBLUE + "   MP")
        print(
            bcolors.FAIL + "                  ______________________________" + bcolors.OKBLUE + "         __________" + bcolors.ENDC)
        print(
            bcolors.BOLD + self.name + alignment_string + bcolors.FAIL + hp_align_str+str(
                self.hp) + "/"+str(self.maxhp)+maxhp_align_str+"  |"+hp_line*"▓"+(30-hp_line)*" "+"|" + bcolors.OKBLUE + " "+mp_align_str+str(self.mp)+"/"+str(self.maxmp)+maxmp_align_str+" |"+mp_line*"▓"+(10-mp_line)*" "+"|" + bcolors.ENDC)
