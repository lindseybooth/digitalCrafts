# class Character:
#     def __init__(self, health, power):
#         self.health = health
#         self.power = power
        
#     def attack(self, hero, goblin):
#         self.health -= self.power
#         print("You do {} damage to the {}.".format())

class Goblin:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
        print(self.health, self.power)

    def attack(self, hero):
        hero.health -= self.power
        if hero.health <= 0:
            print("the hero is dead")
        else:
            print("The goblin does {} damage to the hero.".format(goblin.power))

class Hero:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
        print(self.health,self.power)

    def attack(self, goblin):
        # Hero attacks goblin
        goblin.health -= self.power
        if goblin.health <= 0:
            print("The goblin is dead.")
        else:
            print("The hero does {} damage to the goblin.".format(hero.power)
        
# goblin = Goblin(10,2)
# hero = Hero(10, 4)

# goblin1.attack(Hero)
# hero1.attack(Goblin)





# def main()
#     goblin = Goblin(6, 2)
#     print(goblin.name)
#     print(goblin.health)
#     print(goblin.power)

#     hero = Hero(10, 5)
#     print(hero.name)
#     print(hero.health)
#     print(hero.power)

#     Character.attack(hero, goblin)

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             hero.attack(goblin)
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()