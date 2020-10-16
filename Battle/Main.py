from Battle.Classes.Game import Person, bcolors
from Battle.Classes.magic import Spell

# Create black magic

fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("thunder", 10, 100, "Black")
blizzard = Spell("blizzard", 10, 100, "Black")
meteor = Spell("meteor", 20, 200, "Black")
quake = Spell("quake", 14, 140, "Black")
# Create white magic

cure = Spell("Cure", 12, 100, "White")
cura = Spell("Cura", 18, 200, "White")

magic = [{'name': 'fire', 'cost': 9, 'dmg': 90},
         {'name': 'Thunder', 'cost': 18, 'dmg': 180},
         {'name': 'blizzard', 'cost': 25, 'dmg': 250}]
player = Person(600, 60, 56, 45, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1000, 65, 45, 25, magic)
running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks" + bcolors.ENDC)
while running:
    print(bcolors.OKGREEN + "+++++++++++++++++++++++++++" + bcolors.ENDC)
    player.choose_action()
    print(bcolors.OKGREEN + "+++++++++++++++++++++++++++" + bcolors.ENDC)

    # running = False
    choice = input("Choose Action: ")
    index = int(choice) - 1
    print("You chose", choice)
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for damage: ", dmg)
        print("Enemy hp is ", enemy.get_hp())
    elif index == 1:
        print(bcolors.OKBLUE + "+++++++++++++++++++++++++++" + bcolors.ENDC)

        player.choose_magic()
        print(bcolors.OKBLUE + "+++++++++++++++++++++++++++" + bcolors.ENDC)
        print("Your magic pts: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC)

        magic_choice = input("Choose magic: ")
        magic_index = int(magic_choice) - 1
        spell = player.magic[magic_index]
        magic_damage = spell.generate_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_damage)
        print(bcolors.OKBLUE + "\n" + spell.name + " with damage: " + str(magic_damage) + bcolors.ENDC)
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
        running = False
        break

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for damage :", enemy_dmg)
    print("========================================")
    print("Enemy Hp:" + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)
    print("Your Hp:" + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    print("Your magic pts: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC)

    print("Your hp is ", player.get_hp())

    if player.get_hp() == 0:
        print(bcolors.FAIL + "You Lost" + bcolors.ENDC)
        running = False
        break

    '''
    
    print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_spell_damage(1))
print(player.generate_spell_damage(0))

    '''
