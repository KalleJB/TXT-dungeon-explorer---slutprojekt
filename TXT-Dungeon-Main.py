# imports
import sys
import os
import random

# classes

class Player:
    def __init__(self, name, power, hitChance, parryChance, tauntChance, health, defence) -> None:
        self.name = name
        self.points = 0
        self.power = power
        self.hitChance = hitChance
        self.parryChance = parryChance
        self.tauntChance = tauntChance
        
        self.stun = False
        self.stunChance = 0
        self.bleed = False
        self.bleedCounter = 0

        self.maxHealth = health
        self.health = health
        self.defence = defence

    def add_points(self, amount):
        self.points += amount

    def attack(self, target):
        pass

    def defend(self, target):
        pass

    def add_stunChance(self, change):
        self.stunChance += change
    
    def bleedCounter_up(self):
        self.bleedCounter += 1
        if self.bleedCounter == 3:
            self.bleed = False
            self.bleedCounter = 0

    def remove_bleed(self):
        self.bleed = False

    def print_test(self):
        print(self.stunChance)



class Enemy:
    def __init__(self, name, pointGain, power, critChance, health, defence, id ) -> None:
        self.name = name
        self.pointGain = pointGain
        self.power = power
        self.critChance = critChance
        self.maxHealth = health
        self.health = health
        self.defence = defence
        self.id = id 

    def attack(target):
        pass

    def defend(target):
        pass

class Item:
    def __init__(self, name, id, stackable) -> None:
        self.name = name
        self.id = id
        self.stackeble = stackable

    def drop(target):
        pass

class Room:
    def __init__(self, enemies, loot, connectedRooms) -> None:
        self.enemies = enemies
        self.loot = loot
        self.connectedRooms = connectedRooms 

    def spawnEnemies():
        pass

    def clearRoom():
        pass

class Weapon(Item):
    def __init__(self, name, id, stackable, damage, critChance, special, stunChance, bleedChance) -> None:
        super().__init__(name, id, stackable)
        self.damage = damage
        self.critChance = critChance
        self.special = special
        self.stunChance = stunChance 
        self.bleedChance = bleedChance

    def attack(target):
        pass

    def add_bleed(self, opponent):
        opponent.bleed = True

class Sheild(Weapon):
    def __init__(self, name, id, stackable, damage, critChance, special, size, defence) -> None:
        super().__init__(name, id, stackable, damage, critChance, special)
        self.size = size
        self.defence = defence

class Consumable(Item):
    def __init__(self, name, id, stackable, healthGain, powerGain, defenceGain) -> None:
        super().__init__(name, id, stackable)
        self.healthGain = healthGain
        self.powerGain = powerGain
        self.defenceGain = defenceGain
    
    def use():
        pass

class Armour(Item):
    def __init__(self, name, id, stackable, healthUp, powerUp, defenceUp) -> None:
        super().__init__(name, id, stackable)
        self.healthUp = healthUp
        self.powerUp = powerUp
        self.defenceUp = defenceUp

    def wear():
        pass


# functions


def start_game():
    print("############################")
    print('# Welcome to Dont Wake Up! #')
    print("############################")
    print('- Confirm your commands by typing the letter in the [box].')
    print('- [x] Wake up')

    start = input('> ')
    if start.lower() == "x":
        os.system("cls")
        return True
    else:
        os.system('clear')

def choose_name():
    print("You open you eyes but don't see a thing, feeling as if they've been glued shut.\nWhile trying to remeber why you're here, you realize you dont even know your name...")
    print("\nWhats your name?")
    name = input('> ')

    os.system('cls')
    print(f'{name}... That feels familiar.')
    return name

def first_room(player):
    print("Regaining some of your vision lets you see the walls of the room containing you. \nThey're made of damp cobblestone rock you've never seen before. \nFinding our why you are here is starting to get urgent.")
    print("\nYou find a small wooden door on one of the walls.")
    print("Before you have time take your first step, a voice in your head tells you to imagine a gift.")
    choose_boon(player)
    print("[x] Open door")
    door = input("> ")
    if door.lower() == "x":
        os.system("cls")
    


def points():
    pass

def enterRoom():
    print("\n" + '='*35)
    print("What would you like to do?")
    print("[x] Fight ")
    print("[y] Flee ")
    print("[z] Interact ")
    
    acceptable_actions = ["x", "y", "z"]
    action = input("> ")
    while action not in acceptable_actions:
        print("Unknown action, do something else.\n")
        action = input("> ")
        #os.system('cls')

    os.system('cls')
    if action.lower() == "x":
        fight()
    elif action.lower() == "y":
        flee()
    elif action.lower() == "z":
        interact()
    else:
        pass 

def choose_boon(player):
    print("Closing your eyes, your vision suddenly becomes more vivid.")
    print("Imagine a gift.")

    boon_name_list = ["+1 stunChance", "+1 parryChance"]
    #boon_list = [player.add_stunChance(2)]

    print(player.print_test())
    print(f"[x] {boon_name_list[0]}")
    #print(f"[y] {}")
    #print(f"[z] {}")

    acceptable_choices = ["x", "y", "z"]
    choice = input("> ")
    while choice.lower() not in acceptable_choices:
        print("Unknown action, do something else.\n")
        choice = input("> ")

    if choice == "x":
        player.stunChance += 1

    print(f"As you imagine the gift in your head, you feel power surging trough you.")
    print(f"{boon_name_list[0]} gained.")
    print(player.print_test())
    #print(x power gained, x def gained, x def lost etc)
    

def fight():
    pass



# main
def main():
    while True:
        playing = start_game()
        if playing == True:
            break
    
    # Skapa spelkaraktären och namnge den 
    player_power = 3
    player_health = 10
    player_defence = 1
    hit_chance = 60
    parry_chance = 50
    tauntChance = 50
    player = Player(choose_name(), player_power, hit_chance, parry_chance, tauntChance, player_health, player_defence)

    first_room(player)

    
    while True:
        enterRoom()


if __name__ == "__main__":
    main()