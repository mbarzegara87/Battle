# I want to test 2

from Classes.Game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item
import random



# Create black magic

fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("thunder", 10, 100, "Black")
blizzard = Spell("blizzard", 10, 100, "Black")
meteor = Spell("meteor", 20, 200, "Black")
quake = Spell("quake", 14, 140, "Black")
# Create white magic

cure = Spell("Cure", 12, 100, "White")
cura = Spell("Cura", 18, 200, "White")
# items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
elixir = Item("Elixir", "elixir", "Restores Party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "deals 500 damage", 500)

player_items = [{"item": potion, "quantity": 5}, {"item": elixir, "quantity": 5}, {"item": grenade, "quantity": 5}]
player = Person(600, 60, 56, 45, [fire, thunder, blizzard, meteor, cure, cura], player_items,"Valos")
player2 = Person(600, 60, 56, 45, [fire, thunder, blizzard, meteor, cure, cura], player_items,"Nick")
player3 = Person(600, 60, 56, 45, [fire, thunder, blizzard, meteor, cure, cura], player_items,"Robot")
players=[player,player2,player3]

enemy = Person(999, 65, 45, 25, [], [],"Monster")
running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks" + bcolors.ENDC)
while running:
    print("\n")
    for player in players:
        player.get_stats()
    enemy.get_enemy_stats()
    for player in players:
        print(bcolors.OKGREEN + "+++++++++++++++++++++++++++" + bcolors.ENDC)
        player.choose_action()
        print(bcolors.OKGREEN + "+++++++++++++++++++++++++++" + bcolors.ENDC)

        # running = False
        choice = input("@"+player.name+"! Choose Action: ")
        index = int(choice) - 1
        print(player.name+" chose", choice)
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(player.name+" attacked for damage: ", dmg)
            print("Enemy hp is ", enemy.get_hp())
        elif index == 1:
            print(bcolors.OKBLUE + "+++++++++++++++++++++++++++" + bcolors.ENDC)

            player.choose_magic()
            print(bcolors.OKBLUE + "+++++++++++++++++++++++++++" + bcolors.ENDC)
            print(player.name+"'s magic pts: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC)

            magic_choice = input("Choose magic: ")
            magic_index = int(magic_choice) - 1
            if magic_index == -1:
                continue
            spell = player.magic[magic_index]
            magic_damage = spell.generate_damage()

            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)
            if spell.type == "White":
                player.take_damage(-magic_damage)
                print(bcolors.OKGREEN + "\n" + spell.name + " heals: " + str(magic_damage) + bcolors.ENDC)
            elif spell.type == "Black":
                enemy.take_damage(magic_damage)
                print(bcolors.OKBLUE + "\n" + spell.name + " with damage: " + str(magic_damage) + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("choose item")) - 1
            if item_choice == -1:
                continue
            item = player.items[item_choice]
            if item["item"].type == "potion" and item["quantity"] > 0:
                player.take_damage(-item["item"].prop)
                item["quantity"] = item["quantity"] - 1
                print(bcolors.OKGREEN + "\n" +player.name+":"+ item["item"].name + " heals: " + str(item["item"].prop) + bcolors.ENDC)

            elif item["item"].type == "elixir" and item["quantity"] > 0:
                player.take_damage(-item["item"].prop)
                player.reduce_mp(-item["item"].prop)
                item["quantity"] = item["quantity"] - 1

                print(bcolors.OKGREEN + "\n" + item["item"].name + " heals: " + str(item["item"].prop) + bcolors.ENDC)
                print(bcolors.OKBLUE + "\n" + item["item"].name + " Fills potion by: " + str(
                    item["item"].prop) + bcolors.ENDC)
            elif item["item"].type == "attack" and item["quantity"] > 0:
                enemy.take_damage(item["item"].prop)
                item["quantity"] = item["quantity"] - 1
                print(bcolors.OKGREEN + player.name+" attacked with " + item["item"].name + " for damage: " + str(
                    item["item"].prop) + bcolors.ENDC)
            elif item["quantity"] <= 0:
                print(bcolors.FAIL + player.name+", you don't have enough from this item" + bcolors.ENDC)
                continue

        if enemy.get_hp() == 0:
            print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
            running = False
            break

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    random_player_number=random.randrange(0,len(players)-1)
    player=players[random_player_number]
    player.take_damage(enemy_dmg)
    print("Enemy attacked "+player.name+" for damage :", enemy_dmg)
    print("========================================")
    print("Enemy Hp:" + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)


    print(player.name+"'s hp is ", player.get_hp())

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
