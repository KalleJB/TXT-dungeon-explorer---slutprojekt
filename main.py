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
    def __init__(self, name, id, stackable, damage, crit_chance, special, stun_chance, bleedChance) -> None:
        super().__init__(name, id, stackable)
        self.damage = damage
        self.crit_chance = crit_chance
        self.special = special
        self.stun_chance = stun_chance 
        self.bleedChance = bleedChance

    def attack(target):
        pass

    def add_bleed(self, opponent):
        opponent.bleed = True

class Sheild(Weapon):
    def __init__(self, name, id, stackable, damage, crit_chance, special, size, defence) -> None:
        super().__init__(name, id, stackable, damage, crit_chance, special)
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

class Enemy:
    def __init__(self, name, point_gain, power, hit_chance, crit_chance, health, defence, variant, id ) -> None:
        self.name = name
        self.point_gain = point_gain
        self.power = power
        self.hit_chance = hit_chance
        self.crit_chance = crit_chance
        self.max_health = health
        self.health = health
        self.defence = defence
        self.variant = variant
        self.id = id 

    def attack(target):
        pass

    def defend(target):
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
    os.system("cls")
    print("[x] Open door")
    door = input("> ")
    if door.lower() == "x":
        os.system("cls")
    
###########################    
def spawn_common(lvl, name):
    point_gain = 10 * lvl
    power = 1 + lvl
    hit_chance = 40
    crit_chance = 1
    max_health = 6 + lvl
    health = max_health
    defence = 0
    variant = "common"
    id = lvl

    return Enemy(name, point_gain, power, hit_chance, crit_chance, health, defence, variant, id)
    
def spawn_strange(lvl, name):
    point_gain = 30 * lvl
    power = 3 + lvl
    hit_chance = 60
    crit_chance = 1
    max_health = 6 + lvl * 2
    health = max_health
    defence = 2
    variant = "strange"
    id = lvl

    return Enemy(name, point_gain, power, hit_chance, crit_chance, health, defence, variant, id)

def spawn_legendary(lvl, name):
    point_gain = 100 * lvl
    power = 7 + lvl * 2
    hit_chance = 70
    crit_chance = 10
    max_health = 15 + lvl * 3
    health = max_health
    defence = lvl 
    variant = "legendary"
    id = lvl

    return Enemy(name, point_gain, power, hit_chance, crit_chance, health, defence, variant, id)

def spawn_enemy(lvl):

    # Insert API name generator here
    # Monster scales with lvl
    name = "Gustavo"

    # Determines type
    dice_roll = random.randint(0, 100)
    # 20% chance
    if 0 <= dice_roll < 20:
        return spawn_strange(lvl, name)
    # 75% chance
    elif 20 <= dice_roll <= 95:
        return spawn_common(lvl, name)
    # 5% chance
    elif 95 < dice_roll <= 100:
        return spawn_legendary(lvl, name)
###########################

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
    
    os.system('cls')
    if picked_boon.value > 0:
        print(f"As you imagine the gift in your head, you feel power surging through you.")
        print(f"{picked_boon.value} {picked_boon.effect} gained.")
    else:
        print("As you imagine the gift in your head, you feel an aching pain in your soul.")
        print(f"{picked_boon.value} {picked_boon.effect} lost.")
    
    print("\n\n[x]  Continue")
    input("> ")
    return

###########################
def show_stats(enemy):

    # print enemy and player stats  
    os.system("cls")
    print("___________________ \n")
    print("[x] See MY stats")
    print("[y] See ENEMY stats")
    print("[z] Go back")
    print("___________________")
    aceptable_answers = ["x", "y", "z"]
    answer = input("> ")


    if answer in aceptable_answers:
        if answer.lower() == "x":
            pass
        elif answer.lower() == "y":
            pass
        elif answer.lower() == "z":
            return  

def player_attack(enemy):
    print(enemy.health)
    input("")

def player_defend(enemy):
    pass

def player_turn(enemy):
    while True:
        os.system("cls")
        print(f"You're up against {enemy.name}, a {enemy.variant} enemy.")
        print("Whats your next move?")
        print("_____________ \n")
        print("[x] Attack")
        print("[y] Defend")
        print("[z] See stats")
        print("_____________")
        aceptable_answers = ["x", "y", "z"]
        answer = input("> ")


        if answer in aceptable_answers:
            if answer.lower() == "x":
                player_attack(enemy)
            elif answer.lower() == "y":
                player_defend(enemy)
            elif answer.lower() == "z":
                show_stats(enemy)
        else:
            pass

def enemy_turn():
    pass

def fight(enemy):

    show_stats(enemy)
    
    player_turn(enemy)
    enemy_turn()

###########################

def game_over():
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

    # Main game loop lol
    lvl = 1
    while True:
        enemy = spawn_enemy(lvl)
        fight(enemy)
        choose_boon()
        lvl += 1



if __name__ == "__main__":
    main()