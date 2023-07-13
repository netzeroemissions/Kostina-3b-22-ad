class Character:
    def __init__(self, name, level, health, attack, guard):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.guard = guard

    def damage(self, power):
        self.health -= power

    def upgrade(self,):
        self.level += 1
        self.health *= 1.1
        self.attack *= 1.1

character_1 = Character('Бэтмэн', 1, 100, 30, 11)
character_2 = Character('Джокер', 2, 100, 14, 9)

for round in range(1, 4):
    print(character_1.name, 'vs', character_2.name, 'раунд', round)
    damage_1 = max(0, character_1.attack - character_2.guard)
    damage_2 = max(0, character_2.attack - character_1.guard)
    character_1.damage(damage_2)
    character_2.damage(damage_1)
    print(character_1.name, 'навредил', character_2.name, 'на', damage_1)
    print(character_2.name, 'навредил', character_1.name, 'на', damage_2)

if character_1.health > character_2.health:
    print('По итогам трех раундов победу одержал', character_1.name)
elif character_2.health > character_1.health:
    print('По итогам трех раундов победу одержал', character_2.name)
else:
    print('В этот раз никто не круче')