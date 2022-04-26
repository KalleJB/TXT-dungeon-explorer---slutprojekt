# imports

import sys
import os
import random


# classes

class Player:
    def __init__(self, name, power, hit_chance, parry_chance, taunt_chance, health, defence) -> None:
        self.name = name
        self.points = 0
        self.power = power
        self.hit_chance = hit_chance
        self.parry_chance = parry_chance
        self.taunt_chance = taunt_chance
        
        self.stun = False
        self.stun_chance = 0
        self.bleed = False
        self.bleed_counter = 0

        self.max_health = health
        self.health = health
        self.defence = defence

    def add_points(self, amount):
        self.points += amount

    def attack(self, target):
        pass

    def defend(self, target):
        pass

    def bleed_counter_up(self):
        self.bleed_counter += 1
        if self.bleed_counter == 3:
            self.bleed = False
            self.bleed_counter = 0

    def remove_bleed(self):
        self.bleed = False
    
    def modify_boon(self, boon):
        # boon är en gåva
        # den adderar/subtraherar nånting till/från ett visst atr
        # vi behöver lista ut vilken effekten är och sen välja
        # rätt attribut
        
        # boon.effect # ger oss vilken variabel som ska ändras
        setattr(self, boon.effect, getattr(self, boon.effect) + boon.value)
        # setattr(object, variablenamn, value)





class Enemy:
    def __init__(self, name, pointGain, power, critChance, health, defence, id ) -> None:
        self.name = name
        self.pointGain = pointGain
        self.power = power
        self.critChance = critChance
        self.max_health = health
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
    def __init__(self, name, id, stackable, damage, critChance, special, stun_chance, bleedChance) -> None:
        super().__init__(name, id, stackable)
        self.damage = damage
        self.critChance = critChance
        self.special = special
        self.stun_chance = stun_chance 
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

class Boon:
    def __init__(self, name, effect, value) -> None:
        self.name = name # nått ballt namn på boonet, typ Shalyas Favor som ger mer health
        self.effect = effect # sträng som innehåller variabelnamnet, t ex "self.health"
        self.value = value # talet som ska ändra nånting hos player
        #self.flavour_text
    def __str__(self) -> str:
        return f"{self.name}"
        #flavour_text
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

def choose_boon(player : Player):
    boons = [Boon("Shalyas gift", "health", 3), 
                Boon("Grungi's Might", "power", 3), 
                Boon("Valayas decadence", "stun_chance", 5),
                Boon("Ymirs blessing", "power", 7),
                Boon("Draculas might", "health", -2)]

    avaliable_boons = []
    for i in range(3):
        avaliable_boons.append(boons[random.randint(0, len(boons) - 1)])

    print("Closing your eyes, your vision suddenly becomes more vivid.")
    print("You imagine a some gifts.")
    i = 1
    print("______________________ \n")
    for i, boon in enumerate(avaliable_boons):
        print(f'[{i}]  {boon}')
    
    print("______________________")
    print("Manifest a boon with their index.")

    while True:
        boon_choice = int(input("> "))
        if 0 <= boon_choice <= 2:
            picked_boon = avaliable_boons[boon_choice]
            player.modify_boon(picked_boon)
            print("\n")
            break
        else:
            print("You get a stroke.")
    
    
    if picked_boon.value > 0:
        print(f"As you imagine the gift in your head, you feel power surging through you.")
        print(f"{picked_boon.value} {picked_boon.effect} gained.")
    else:
        print("As you imagine the gift in your head, you feel an aching pain in your soul.")
        print(f"{picked_boon.value} {picked_boon.effect} lost.")
    
    print("\n\n [x]  Continue")
    input("> ")
    return


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
    taunt_chance = 50
    player = Player(choose_name(), player_power, hit_chance, parry_chance, taunt_chance, player_health, player_defence)

    first_room(player)

    # Main game LOOP
    # Skapa fiende
        # Player turn
        # Enemy turn
    # Choose boon




if __name__ == "__main__":
    main()