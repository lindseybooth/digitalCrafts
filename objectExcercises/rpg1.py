# class Character:
#     def __init__(self, health, power):
#         self.health = health
#         self.power = power
        
#     def attack(self, hero, goblin):
#         self.health -= self.power
#         print("You do {} damage to the {}.".format())

class Goblin:
    def __init__ (self, health, power):
        #goblin attacks hero
        self.health = health
        self.power = power
        print(self.health, self.power)

    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {} damage to the hero.".format(self.power))
        if hero.health <= 0:
            print("the hero is dead")

    def alive(self):
        if self.health >= 0:
            return True
        else :
            return False

    def status(self):
        if self.health >= 0:
            print("The goblin is still alive")
        else:
            print("The goblin is dead.")
            

class Hero:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
        print(self.health, self.power)

    def attack(self, goblin):
        # Hero attacks goblin
        goblin.health -= self.power
        print("The hero does {} damage to the goblin.".format(self.power))

    def alive(self):
        if self.health >= 0:
            return True
        else :
            return False

    def status(self):
        if self.health >= 0:
            print("The hero is still alive.")
        else:
            print("The hero is dead.")


def main():
   
    goblinName = Goblin(20, 3)
    heroName = Hero(25, 8)

    goblinName.status()

    while goblinName.alive() and heroName.alive():
        print("The hero has {} health and {} power.".format(heroName.health, heroName.power))
        print("The goblin has {} health and {} power.".format(goblinName.health, goblinName.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            heroName.attack(goblinName)
            print("After attack, the goblin's health is: {} {}".format(goblinName.health, goblinName.alive()))
            if goblinName.alive() == False:
                goblinName.status()
                break
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblinName.alive():
            # Goblin attacks hero
            goblinName.attack(heroName)
            if heroName.alive() == False:
                heroName.status()

main()

