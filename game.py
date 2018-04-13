import msvcrt
import os
import time

from Hero import *
from Enemy import *
from Statistic import *

enemy_list = ["Poring", "Thief bug", "Familiar"]
farming_speed = 1
time_wrap = 0.1


def information():
    try:
        os.system('cls')
    except:
        os.system('clear')
    hero.show_hero()
    action_menu()


def action_menu():
    print("Choose option\n"
          "1: eat\n"
          "2: find enemy\n"
          "3: jerk off\n"
          "4: show statistics\n"
          "x: Exit")


def fight():
    def fight_info(name_info, dmg, exp, zen):
        hero.change_health(-dmg)
        hero.get_exp(exp)
        hero.change_zeny(zen)
        information()
        print(name_info + " got rekt")

    pr = ''
    # print("Searching for pedrilas")
    while True:
        chance = random.randint(1, 10)
        time.sleep(farming_speed*time_wrap)
        pr += "#"
        if len(pr) > 23:
            print('Dungeon found. You see massive "The Doors" (not dead musicians)')
            print("\t\tYOU ARE NO PREPARED\n" + "\t\t" + "Tікай з городу - тобi пiзда".title())
            continue

        print(pr, end='\r')
        if chance == 5:
            choose_fight = random.randint(1, len(enemy_list)+1)
            if choose_fight == 1:
                statistic.increase_poring(1)
                fight_info(enemy_list[0], poring.damage, poring.exp, poring.zeny)
            elif choose_fight == 2:
                statistic.increase_thiefbug(1)
                fight_info(enemy_list[1], thief_bug.damage, thief_bug.exp, thief_bug.zeny)
            elif choose_fight == 3:
                statistic.increase_familiar(1)
                fight_info(enemy_list[2], familiar.damage, familiar.exp, familiar.zeny)
            else:
                hero.change_health(-10)
                statistic.increase_butylka(1)
                information()
                print("Found butylka and sat on it")
                break
            break


# -----------MAIN-----------------


poring = Enemy("Poring", 150, 5, 10, "jellopy")
thief_bug = Enemy("Thief bug", 180, 7, 15, "skin")
familiar = Enemy("Familiar", 200, 8, 22, "wing")

name = input("Create new hero\n"
             "Enter hero name: ")
hero = Hero(name, "Human")
statistic = Statistics(0, 0, 0, 0)

information()

while True:
    # os.system('cls')
    try:
        choice = msvcrt.getch().decode('utf-8')
    except UnicodeDecodeError:
        pass
    else:
        if choice == '1':
            hero.change_zeny(-5)
            if hero.zeny >= 5:
                hero.change_pisos(1)
            information()
            print("Pisos polished")
        elif choice == '2':
            fight()
        elif choice == '3':
            hero.change_pisos(-1)
            if hero.pisos >= 0:
                hero.change_health(11)
            information()
            print("Masturbated so hard!!!")
        elif choice == '4':
            statistic.show_statistics()
        if choice == 'x':
            sys.exit(0)
