#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random
from random import randrange
from random import randint
from random import uniform
    
class Character:
    def __init__(self,health,power):   
        self.name = ""
        self.health = health
        self.power = power
        self.player = True
        self.crit_chance = True
        self.coins = 100
        self.itemsinventory = []
        self.armorsinventory = []
        self.weaponsinventory = []
        self.armor = 0 
        self.evade = 0



    def attack(self,enemy):
        # player attack
        if self.player == True:
            if self.crit_chance == True: 
                if randint(1,5) == 5:
                    if self.name == "Hero-sama":
                        enemy.health -= float(self.power * 2)
                        print(f"{self.name} critical for {float(self.power*2)} damage to {enemy.name}.")
                    elif self.name == "Pasion the Beast King":
                        enemy.health -= float(self.power * 1.75)
                        print(f"{self.name} critical for {float(self.power*2)} damage to {enemy.name}.")                       
                    else:
                        enemy.health -= float(self.power * 1.5)
                        print(f"{self.name} critical for {float(self.power*1.5)} damage to {enemy.name}.")
                else:
                    enemy.health -= self.power
                    print(f"{self.name} did {self.power} damage to {enemy.name}.")
            else:
                enemy.health -= self.power
                print(f"{self.name} did {self.power} damage to {enemy.name}.")
                if enemy.health <= 0 and enemy.name != "Zomebie Lord":
                    print(f"{self.name} has slain {enemy.name}.")
                    self.coins += enemy.bounty
                    print(f"{self.name} have {self.coins} coins")

                    main(enemylist[randint(0, 2)])

        # enemy attack
        else:
            if enemy.evade > 0:
                number = round(uniform(0.1,(1.0 - float(0.05 * enemy.evade))),2)
                if number != float(0.1) and number <= float(0.2):
                    print(f"{enemy.name} evaded {self.name} hit!")
                elif enemy.evade == self.power:
                    print(f"{enemy.name} dodged {self.name} attack.")
                else:
                    enemy.health -= self.power
                    print(f"{self.name} did {self.power} damage to {enemy.name}. ")

            if enemy.armor > 0:
                if enemy.armor >= self.power:
                    print(f'{enemy.name} armor tanked his hit. {enemy.name} received no damage.')
                elif enemy.armor < self.power:
                    enemy.health -= (self.power - enemy.armor)
                    print(f"{self.name} did {self.power} damage to {enemy.name}. ")
                else:
                    enemy.health -= self.power
                    print(f"{self.name} did {self.power} damage to {enemy.name}. ")                    
            if self.crit_chance == True:
                if randint(1,5) == 5:                    
                    enemy.health -= float(self.power * 1.5)
                    print(f"{self.name} critical for {float(self.power*1.5)} damage to {enemy.name}.")
                else:
                    enemy.health -= self.power
                    print(f"{self.name} did {self.power} damage to {enemy.name}.")
            else:
                enemy.health -= self.power
                print(f"{self.name} did {self.power} damage to {enemy.name}.")
            if enemy.health <=0:
                print("You are dead.")

    def purchases(self):
        while True:
            shopping = input(f"Would {self.name} like to go shopping? (Yes/No) ")
            if shopping == 'Yes':
                print(f"You have {self.coins} coins")
                buying_options = input("What do you want to buy? (Items, Armors, Weapons) ")
                if buying_options == 'Items':
                    for key in itemsStore:
                        print(f"{key} = {itemsStore[key]}")
                    items_tobuy = input('What items would you like to buy? ')
                    if items_tobuy in itemsStore.keys() and itemsStore[items_tobuy] < self.coins:
                        self.coins -= itemsStore[items_tobuy]
                        print(f"{self.name} bought {items_tobuy}.")
                        self.itemsinventory.append(items_tobuy)
                        print(f"{self.name} add {items_tobuy} to items inventory.")
                        continue_shopping = input(f"Do you want to continue shopping? (Yes/No) ")
                        if continue_shopping == "Yes":
                           Character.purchases(self)
                        elif continue_shopping == "No":
                            main(enemylist[randint(0, 2)])
                        else:
                            print("Invalid Input. Please type Yes or No. ")

                    else:                   
                        print("Sorry, you were unable to purchase any items.")
                        buy_others = input("Do you want to see the buying options again? (Yes/No) ")
                        if buy_others == "Yes":
                            Character.purchases(self)
                        elif buy_others == "No":
                            main(enemylist[randint(0, 2)])
                        else:
                            print("Invalid Input. Please type Yes or No. ")       

                elif buying_options == 'Armors':
                    for key in armorStore:
                        print(f"{key} = {armorStore[key]}")
                    armors_tobuy = input('What armor would you like to buy? ')
                    if armors_tobuy in armorStore.keys() and armorStore[armors_tobuy] < self.coins:
                        self.coins -= armorStore[armors_tobuy]
                        print(f"{self.name} bought {armors_tobuy}.")
                        self.armorsinventory.append(armors_tobuy)
                        print(f"{self.name} add {armors_tobuy} to armors inventory.")
                        continue_shopping = input(f"Do you want to continue shopping? (Yes/No) ")
                        if continue_shopping == "Yes":
                            Character.purchases(self)
                        elif continue_shopping == "No":
                            main(enemylist[randint(0, 2)])
                        else:
                            print("Invalid Input. Please type Yes or No. ")
                    else:
                        print("Sorry, you were unable to purchase any armor.")
                        buy_others = input("Do you want to see the buying options again? (Yes/No) ")
                        if buy_others == "Yes":
                            Character.purchases(self)
                        elif buy_others == "No":
                            main(enemylist[randint(0, 2)])
                        else:
                            print("Invalid Input. Please type Yes or No. ")

                elif buying_options == "Weapons":
                    for key in weaponStore:
                        print(f"{key} = {weaponStore[key]}")
                    weapons_tobuy = input("What weapon would you like to buy? ")
                    if weapons_tobuy in weaponStore.keys() and weaponStore[weapons_tobuy] < self.coins:
                        self.coins -= weaponStore[weapons_tobuy]
                        print(f"{self.name} bought {weapons_tobuy}.")
                        self.armorsinventory.append(weapons_tobuy)
                        print(f"{self.name} add {wepaon_tobuy} to weapons inventory.")
                        continue_shopping = input(f"Do you want to continue shopping? (Yes/No) ")
                        if continue_shopping == "Yes":
                            Character.purchases(self)
                        elif continue_shopping == "No":
                            main(enemylist[randint(0, 2)])
                        else:
                            print("Invalid Input. Please type Yes or No. ")
                    else:
                        print("Sorry, you were unable to purchase any weapons.")
                        buy_others = input("Do you want to see the buying options again? (Yes/No) ")
                        if buy_others == "Yes":
                            Character.purchases(self)
                        elif buy_others == "No":
                            main(enemylist[randint(0, 2)])
                        else:
                            print("Invalid Input. Please type Yes or No. ")                     
                else:             
                    print("Sorry, your input was invalid.")
            elif shopping == "No":
                main(enemylist[randint(0, 2)])
            else:
                print("Sorry, your input was invalid. Please type Yes or No")





    def items_Inventory(self,enemy):
        print(f'Here is what in your item inventory: {self.itemsinventory}')  
        use_item = input("What item would you like to use? ") 
        if use_item == "Super Tonic" and self.player == True:           
            self.health += 10
            self.itemsinventory.remove(use_item)
            print(f'You have healed {self.health} health.')
        if use_item == "Scroll of Teleport" and self.player == True:
            self.evade += 2
            self.itemsinventory.remove(use_item)


                    

        
    def armor_Inventory(self,enemy):
        print(f'Here is what in your armor inventory: {self.armorsinventory}')
        use_armor = input("What item would you like to use? ")
        if use_armor == "Light Armor" and self.player == True:
            self.armor += 2
            self.armorsinventory.remove(use_armor)
            print(f"{self.name} put on some light armor")

        if use_armor == "Heavy Armor" and self.player == True:
            self.armor += 4
            self.armorsinventory.remove(use_armor)
            print(f"{self.name} put on some heavy armor")
        else:
            pass

    
    def weapon_Inventory(self,enemy):
        print(f'Here is what in your weapon inventory: {self.weaponsinventory}')
        use_weapon = input("What item would you like to use? ")
        if use_weapon == "Short Sword":
            self.power += 2
            self.weaponsinventory.remove(use_weapon)
            print(f"{self.name} equip a short sword. ")
        if use_weapon == "Long Sword":
            self.power += 3
            self.weaponsinventory.remove(use_weapon)
            print(f"{self.name} equip a long sword. ")
        else:
            pass


    def print_status(self):
        if self.player == True:
            print(f"{self.name} health: {self.health}, {self.name} power: {self.power}")
        else: 
            print(f"{self.name} health: {self.health}, {self.name} power: {self.power}")
    
    def alive(self):
        return self.health > 0
        

class Hero(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Hero-sama"
        self.player = True
        self.crit_chance = True
        self.coins = 100
        self.armor = 0
        self.evade = 0

class Goblin(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Goblin"
        self.player = False
        self.crit_chance = True
        self.bounty = 10


class Zombie(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Zombie Lord"
        self.player = False
        self.crit_chance = True
        self.bounty = 20
    def alive(self):
        if self.health == float(0.0) or self.health == 0:
            return False
        if self.health < 0:
            self.health += 10
        print(f"{self.name} regenerate 10 health")
    

class Medic(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Moira"
        self.player = True
        self.crit_chance = False
        self.coins = 100
        self.armor = 0
        self.evade = 0
    def print_status(self):
        if randint(1,5) == 5:
            self.health += 2
            print(f"{self.name} healed for 2 health")
        print(f"{self.name} health: {self.health}, {self.name} power: {self.power}")

class Shadow(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Naruto"
        self.player = True
        self.crit_chance = True
        self.coins = 100
        self.armor = 0
        self.evade = 2
    def attack(self,enemy):
        if self.name == "Naruto" and randint(1,10) > 1:
            enemy.power = 0
            print(f"{self.name} uses Kage Bunshin no Jutsu. {enemy.name} killed some shadow clones.")
            super().attack(enemy)
        else:
            super().attack(enemy)

class Dragon(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Smaug"
        self.player = False
        self.crit_chance = True
        self.bounty = 500
    # def attack(self,enemy):


class Beastman(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Matt the Beast King"
        self.player = True
        self.crit_chance = True
        self.animalinstict = True
        self.coins = 100
        self.armor = 0
        self.evade = 0

    def attack(self,enemy):
        if self.animalinstict == True and self.health <= 6:
            if randint(1,4) > 1:
                print(f"{self.name}'s animal instict has been activated. Damage is double at the cost of 1 health.")
                print(f"{self.name} lose 1 health point.")
                self.health -= 1
                enemy.health -= float(self.power*2)
                print(f"{self.name} did {self.power*2} damage to {enemy.name}.")
            else: 
                super().attack(enemy)           
        else:
            super().attack(enemy)




beastman = Beastman(20,5)
medic = Medic(15,2)    
hero = Hero(25,5)
goblin = Goblin(10,2)
zombielord = Zombie(10,1)
shadow = Shadow(10,4)
dragon = Dragon(100,7)
enemylist = [goblin,zombielord,dragon]
playerlist = [hero, medic, shadow, beastman]
itemsStore = {
    'Super Tonic' : 15,
    'Scroll of Teleportation' : 30,
    }
armorStore ={
    'Light Armor' : 75,
    'Heavy Armor' : 150,
    }
weaponStore = {
    'Short Sword' : 50,
    'Long Sword' : 80,
    }


def main(enemy):


    while beastman.alive():
        beastman.print_status()
        enemy.print_status()

        print()
        print("What do you want to do?")
        print(f"1. Fight {enemy.name}.")
        print("2. Do nothing.")
        print("3. Flee.")
        print("4. Return to town to buy some items and equipments.")
        print("5. Use an item.")
        print("6. Put on an armor.")
        print("7. Wield a weapon.")
        print("8. End game.")
        print("> ", end=' ')
        keyinput = input()
        if keyinput == "1":
            beastman.attack(enemy)
        elif keyinput == "2":
            pass
        elif keyinput == "3":
            main(enemylist[randint(0, 2)])
        elif keyinput =="4":
            beastman.purchases()
        elif keyinput == "5":
            beastman.items_Inventory(enemy)
        elif keyinput == "6":
            beastman.armor_Inventory(enemy)
        elif keyinput == "7":
            beastman.weapon_Inventory(enemy)    
        elif keyinput == "8":
            print("Goodbye.")
            exit()
        else:
            print(f"Invalid input {keyinput}")

        if enemy.alive():
            enemy.attack(beastman)

            
main(enemylist[randint(0,2)])
