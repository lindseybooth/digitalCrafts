import random

class Character:
    def __init__(self, health, power, characterName):
        self.health = health
        self.power = power
        self.name = characterName

    def alive(self):
        if self.characterName == "Zombie":
            return True
        if self.health >= 0:
            return True
        else:
            return False

    def attack(self, enemy):
        damageCounter = 1

        if enemy.name == "Shadow":
            myRandom = random.randint(1, 10)
            if myRandom <= 1:
                enemy.health -= self.power
            else:
                print("{} wasn't damaged!".format(enemy.name))
                damageCounter = 0
        else:
            enemy.health -= self.power

        if self.characterName == "Hero":
            myRandom = random.randint(1, 5)
            if damageCounter == 0:
                pass
            elif myRandom <= 2:
                enemy.health -= self.power
                print("{} did double damage!".format(self.name))
                damageCounter = 2

        if enemy.name == "Ogre":
            myRandom = random.randint(1, 10)
            if myRandom <= 3:
                self.health -= damage_coefficient * self.power
                print("{} damaged additional {} points.".format(self.name, damageCounter * self.power))

        if enemy.name == "Medic":
            myRandom = random.randint(1, 5)
            if myRandom <= 2:
                enemy.health += 2
                print("{} recuperated 2 health points.".format(enemy.name))
        
        if enemy.health <=0 and enemy.name != "Zombie":
            print("{} is dead".format(enemy.name))
            self.coins += enemy.bounty
            print("{} collects {} bounty by defeating {}.".format(self.name, enemy.bounty, enemy.name))

        elif enemy.health <= 0 and enemy.name == "Zombie":
            print("{} never dies!".format(enemy.name))
        elif self.health <= 0:
            print("{} is dead.".format(self.name))
   
    def status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))")     

class Hero(Character):
    def __init__ (self, health, power, characterName):
        super().__init__(health, power)
        self.characterName = "Hero"
        self.coins = 0

    def buy(self, item):
        def buy(self, item):
        self.coins -= item.cost
        print("{} coin balance is {}.".format(self.name, self.coins))
        print(item)
        item.apply(self)

class Goblin(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Goblin"
        self.bounty = 5

class Medic(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Medic"

class Shadow(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Shadow"
        self.bounty = 2

class Zombie(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Zombie"

class Ogre(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Ogre"
        self.bounty = 8

class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health = 10
        print("{} health is now {}".format(character.name, character.health))

class Store:
    items = [Tonic()]
    def do_shopping(self, hero):
        
        while True:
            print("{} has {} coin balance.".format(hero.name, hero.coins))
            print("What would you like to do?")
            for i in range(0, len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} for {} coins.".format(i +1, item.name, item.cost))

            print("10. leave.")

            answer = int(input("> "))

            if answer == 10:
                break
            else:
                itemToBuy = Store.items[answer - 1]
                print(itemToBuy)
                hero.buy(itemToBuy)

hero1 = Hero(100,5)
goblin1 = Goblin(10,2)
medic1 = Medic(100,2)
shadow1 = Shadow(1,5)
zombie1 = Zombie(10,2)
ogre1 = Ogre(20,2)
shopping = Store()
tonic = Tonic()

def main(hero, enemy):

    while enemy.alive() and hero.alive():
        hero.status()
        enemy.status()
        
        print("The hero has {} health and {} power.".format(heroName.health, heroName.power))
        print("The goblin has {} health and {} power.".format(goblinName.health, goblinName.power))
        print()
        print("What do you want to do?")
        print("1. fight {}".format(enemy.name))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health >= 0 or enemy.name == "Zombie":
            enemy.attack(hero)
main()

