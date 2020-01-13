import os, random, sys

try:
    text = open("text.txt")
except:
    text = open("text.txt", "w")
    name = raw_input("name: ") 
    text.write("name=" + name)
    text.write("\natk=5")
    text.write("\ndef=5")
    text.write("\nmaxLife=20")
    text.write("\nlvl=0")
    text = open("text.txt")    
    
lines = text.readlines()
name = lines[0].strip().split("=")
attack = lines[1].strip().split("=")
defense = lines[2].strip().split("=")
maxLife = lines[3].strip().split("=")
life = maxLife[1]
level = lines[4].strip().split("=")
player = {name[0]: name[1], attack[0]: int(attack[1]), defense[0]: int(defense[1]), maxLife[0]: int(maxLife[1]), 'life': int(life), level[0]: int(level[1])}
monster = {'atk': 1, 'def': 1, 'life': 10, 'maxLife': 10}
enemy = monster.copy()
player_respond = ""
enemy_respond = ""
text.close()

def show_status():
    if player_respond != "" and enemy_respond != "":
        print("%s and %s" %(player_respond, enemy_respond))

    print(player['name'])
    print("Life: %s Attack: %s Defense: %s max: %s" %(player['life'], player['atk'], player['def'], player['maxLife'])) 
    print("Enemy")
    print("Life: %s Attack: %s Defense: %s" %(enemy['life'], enemy['atk'], enemy['def'])) 

def select_option(enemy_option):
    option = raw_input("Options (1)atk, (2)def, (3)regen: ")

    try:
        option = int(option)
    except ValueError:
        print("Invalid option")
        select_option(enemy_option)

    if option < 4 and option > 0:
        play_process(option, enemy_option)
    else:
        print("Invalid option")
        select_option(enemy_option)

def enemy_option():
    return random.randint(1, 3)

def attack(attacker, defender, defend):
    defender_defense = defender['def'] if defend == True else 0
    attacker_attack = attacker['atk'] - defender_defense
    attacker_attack = attacker_attack if attacker_attack > 0 else 0
    defender['life'] = defender['life'] - attacker_attack

def regen(caster):
    if caster['life'] < caster['maxLife']:
        caster['life'] += 1

def play_process(player_option, enemy_option):
    global player_respond, enemy_respond
    player_defend = False
    enemy_defend = False

    if player_option == 2:
        player_respond = player['name'] + " defends"
        player_defend = True

    if enemy_option == 2:
        enemy_respond = "Enemy defends"
        enemy_defend = True

    if player_option == 3:
        player_respond = player['name'] + " regens"
        regen(player)
    if enemy_option == 3:
        enemy_respond = "Enemy defends"
        regen(enemy)
    
    if player_option == 1:
        player_respond = player['name'] + " attacks"
        attack(player, enemy, enemy_defend)
    
    if enemy_option == 1:
        enemy_respond = "Enemy regens"
        attack(enemy, player, player_defend)

def set_enemy():
    enemy['atk'] = monster['atk'] + player['lvl']
    enemy['def'] = monster['def'] + player['lvl']
    enemy['life'] = monster['life'] + + (2 * player['lvl'])
    enemy['maxLife'] = monster['maxLife'] + (2 * player['lvl'])

def check():
    os.system('cls')
    if player['life'] <= 0:
        print("You died")
        sys.exit()
    
    if enemy['life'] <= 0:
        global player_respond, enemy_respond
        print("Enemy Killed")
        player_respond = ""
        enemy_respond = ""
        player['lvl'] += 1
        player['life'] = player['maxLife']
        save()
        show_mainMenu()

def show_mainMenu():
    print("Main Menu")
    menuOption = raw_input("Continue(1) Exit(2): ")
    if menuOption == "1":
        set_enemy()
    elif menuOption == "2":
        sys.exit()
    else:
        show_mainMenu()

def save():
    text = open("text.txt", "w")
    text.write("name=" + player['name'])
    text.write("\natk=" + str(player['atk']))
    text.write("\ndef=" + str(player['def']))
    text.write("\nmaxLife=" + str(player['maxLife']))
    text.write("\nlvl=" + str(player['lvl']))
    text.close()

set_enemy()
while True:
    show_status()
    eo = enemy_option()
    select_option(eo)
    check()