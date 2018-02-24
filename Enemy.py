class Enemy:
    def __init__(self, foe_name, foe_exp, foe_damage, foe_zeny, foe_loot):
        self.name = foe_name
        self.exp = foe_exp
        self.health = 100
        self.damage = foe_damage
        self.zeny = foe_zeny
        self.card = 1
        self.loot = foe_loot

