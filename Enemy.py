class Enemy:
    def __init__(self, foe_name, foe_exp, foe_health, foe_damage, foe_zeny):
        self.name = foe_name
        self.exp = foe_exp
        self.health = foe_health
        self.damage = foe_damage
        self.zeny = foe_zeny
        self.card = 1

    def drop_loot(self):
        pass
