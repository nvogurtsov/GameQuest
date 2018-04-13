import sys
import random


class Hero:
    def __init__(self, hero_name, hero_race):
        self.name = hero_name
        self.lvl = 1
        self.race = hero_race
        self.health = 100
        self.max_health = self.health
        self.regen = 1
        self.exp = 0
        self.zeny = 0
        self.stats = {"str": 1, "sta": 1, "int": 1, "agi": 1}
        self.pisos = 5
        self.inventory = {}
        self.cards = {}

    def change_health(self, dmg):
        self.health += dmg
        if self.health <= 0:
            print("Your hero died!!"
                  "Try to masturbate much many more")
            sys.exit(1)
        elif self.health > self.max_health:
            self.health = self.max_health

    def change_pisos(self, p):
        if self.pisos + p < 0:
            print("Pisos is bleeding, stop masturbate")
        else:
            self.pisos += p

    def change_zeny(self, new_zeny):
        if self.zeny + new_zeny < 0:
            print("You don't have money, dolbaeb")
        else:
            self.zeny += new_zeny

    def lvl_up(self):
        if self.exp >= 1000:
            st = self.exp // 1000
            self.lvl += st
            self.exp = self.exp % 1000
            self.stats["str"] += st
            self.stats["sta"] += st
            self.stats["int"] += st
            self.max_health += 10

    def get_exp(self, new_exp):
        self.exp = self.exp + new_exp
        self.lvl_up()

    def show_hero(self):
        print("Name: " + self.name + ", Level: " + str(self.lvl) + ", Race: " + self.race)
        print("Health: " + str(self.health) + ", Current exp: " + str(self.exp) + ", Zeny: "
              + str(self.zeny) + ", Pisos status: " + str(self.pisos))
        # self.show_stat()

    def show_stat(self):
        print("STR:" + str(self.stats["str"]) + " STA:" + str(self.stats["sta"]) + " INT:" + str(self.stats["int"]))

    def show_inventory(self):
        print("==== Items ====")
        for item in self.inventory:
            print(item + ": " + str(self.inventory[item]))

        print("==== Cards ====")
        for card in self.cards:
            print(card + ": " + str(self.cards[card]))

    def get_loot(self, foe_loot, foe_name, foe_loot_chance):
        loot_chance = random.randint(1, foe_loot_chance)
        card_chance = random.randint(1, 100)
        # print(loot_chance, card_chance)
        if loot_chance == foe_loot_chance:
            print(foe_loot + " dropped")
            if foe_loot not in self.inventory:
                self.inventory[foe_loot] = 1
            else:
                self.inventory[foe_loot] += 1
        if card_chance == 69:
            print(foe_name + " card dropped")
            if foe_name not in self.cards:
                self.cards[foe_name] = 1
            else:
                self.cards[foe_name] += 1


hero = Hero("asd", "a")

# hero.get_loot("jelopy")
# hero.get_loot("jelopy")
hero.get_loot("bone", "skeleton", 20)
hero.get_loot("apple", "poring", 25)
hero.show_inventory()
