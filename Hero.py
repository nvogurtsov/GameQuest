import sys


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
        self.inventory = []

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
            print("Pisos os bleeding, stop masturbate")
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
        #self.show_stat()

    def show_stat(self):
        print("STR:" + str(self.stats["str"]) + " STA:" + str(self.stats["sta"]) + " INT:" + str(self.stats["int"]))
