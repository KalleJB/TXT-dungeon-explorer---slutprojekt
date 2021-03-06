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
        self.crit_chance = 1
        self.parry_chance = parry_chance
        self.taunt_chance = taunt_chance
        
        self.stun = False
        self.stun_chance = 0
        self.bleeding = False
        self.bleeding_counter = 0
        self.fled = False

        self.max_health = health
        self.health = health
        self.defence = defence

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def bleeding_counter_up(self):
        self.bleeding_counter += 1
        if self.bleeding_counter == 3:
            self.bleeding = False
            self.bleeding_counter = 0

    def remove_bleeding(self):
        self.bleeding = False
    
    def modify_boon(self, boon):
        # boon är en gåva
        # den adderar/subtraherar nånting till/från ett visst atr
        # vi behöver lista ut vilken effekten är och sen välja
        # rätt attribut
        
        # boon.effect # ger oss vilken variabel som ska ändras
        setattr(self, boon.effect, getattr(self, boon.effect) + boon.value)
        # setattr(object, variablenamn, value)
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

        self.stun = False
        self.bleeding = False
        self.bleeding_counter = 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

class Boon:
    def __init__(self, name, effect, value) -> None:
        self.name = name # nått ballt namn på boonet, typ Shalyas Favor som ger mer health
        self.effect = effect # sträng som innehåller variabelnamnet, t ex "self.health"
        self.value = value # talet som ska ändra nånting hos player
        #self.flavour_text
    def __str__(self) -> str:
        return f"{self.name}"
        #flavour_text

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
    def __init__(self, name, id, stackable, damage, crit_chance, special, stun_chance, bleedingChance) -> None:
        super().__init__(name, id, stackable)
        self.damage = damage
        self.crit_chance = crit_chance
        self.special = special
        self.stun_chance = stun_chance 
        self.bleedingChance = bleedingChance

    def attack(target):
        pass

    def add_bleeding(self, opponent):
        opponent.bleeding = True

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

# functions

def start_game():
    os.system("cls")
    print("###################################")
    print('# Welcome to Flamboyant Fighting! #')
    print("###################################")
    print('- Confirm your commands by typing the thing in the [box].')
    print('- If there is no box, do anything.')
    print('- [x] Kick ass')

    start = input('> ')
    if start.lower() == "x":
        os.system("cls")
        return True
    else:
        os.system('clear')

def choose_name():
    print("Hi cutie wanna tell me your name?\n")
    name = input('> ')

    os.system('cls')
    print(f'{name}... That feels familiar.')
    print("My name doesnt matter, but im here to inform you that you're next up.")
    input("> ")
    os.system('cls')
    print("What? You cant remember why you are here?")
    input("> ")
    os.system('cls')
    print("HAHAHA how adorable, of course you cant, no one can.")
    print("Just do what makes sense to you, and make sure to make it fruity.")
    input("> ")
    os.system('cls')
    return name

def first_room(player):
    print("But before we start, why dont you close your eyes and imagine some nice things.")

    choose_boon(player)
    os.system("cls")
    print("Walking trough a damp pinkish hallway you see a door laced with leather. \nYou dont feel to good about it.")
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

def choose_boon(player : Player):
    boons = [Boon("Purple thong", "max_health", 3), 
                Boon("Acrylic nails", "power", 3), 
                Boon("Audacity", "stun_chance", 5),
                Boon("High heels", "power", 2),
                Boon("Bubble tea", "health", -2),
                Boon("Lash extensions", "max_health", 2),
                Boon("Pink lipstick", "hit_chance", 5),
                Boon("Knife", "power", 7),
                Boon("Unidentified liquid", "health", +5),
                Boon("Vape", "crit_chance", 5),
                Boon("Pink thong", "points", 50)]

    avaliable_boons = []
    for i in range(3):
        avaliable_boons.append(boons[random.randint(0, len(boons) - 1)])

    print("Closing your eyes, your vision suddenly becomes more vivid.")
    print("You imagine some nice stuff.")
    i = 1
    print("______________________ \n")
    for i, boon in enumerate(avaliable_boons):
        print(f'[{i}]  {boon}')
    
    print("______________________")
    print("Manifest a boon with their index.")

    aceptable_answers = ["0", "1", "2"]
    while True:
        boon_choice = int(input("> "))
        if str(boon_choice) in aceptable_answers:
            picked_boon = avaliable_boons[boon_choice]
            player.modify_boon(picked_boon)
            print("\n")
            break
        else:
            print("You get a stroke.")
    
    os.system('cls')
    if picked_boon.value > 0:
        print(f"As you imagine the fruity things in your head, you feel power surging through you.")
        print(f"{picked_boon.value} {picked_boon.effect} gained.")
    else:
        print("As you imagine the fruity thing in your head, you feel an aching pain in your soul.")
        print(f"{picked_boon.value} {picked_boon.effect} lost.")
    
    print("\n\n[x]  Continue")
    input("> ")
    return

###########################
def show_player_stats(player):
    while True:
        os.system("cls")
        print(f"{player.name}'s stats:")
        print(f"__________________________ \n") 
        print(f"Points       :  {player.points}") 
        print(f"Power        :  {player.power}") 
        print(f"Health       :  {player.health} / {player.max_health}") 
        print(f"Defence      :  {player.defence}")
        print(f"__________________________ \n") 
        print(f"Hit-chance   :  {player.hit_chance}")
        print(f"Crit-chance  :  {player.crit_chance}")
        print(f"Parry-chance :  {player.parry_chance}")
        print(f"Taunt-chance :  {player.taunt_chance}")
        print(f"Stun-chance  :  {player.stun_chance}")
        print(f"__________________________ \n")
        print("Status effects:")
        if player.stun == True:
            print(f"Stuned       :  Yes")
        else:
            print(f"Stuned       :  No")
        if player.bleeding == True:
            print(f"bleeding     :  Yes")
            print(f"bleeding-counter :  {player.bleeding_counter}")
        else:
            print(f"bleeding     :  No")

        print("\n[z] Go back")
        go_back = input("> ")
        if go_back.lower() == "z":
            os.system("cls")
            return

def show_enemy_stats(enemy):
    while True:
        os.system("cls")
        print(f"{enemy.name}'s stats:")
        print(f"__________________________ \n") 
        print(f"Point-gain   :  {enemy.point_gain}")
        print(f"Power        :  {enemy.power}") 
        print(f"Health       :  {enemy.health} / {enemy.max_health}") 
        print(f"Defence      :  {enemy.defence}")
        print(f"Variant      :  {enemy.variant}")
        print(f"__________________________ \n") 
        print(f"Hit-chance   :  {enemy.hit_chance}")
        print(f"Crit-chance   :  {enemy.crit_chance}")
        #print(f"Parry-chance :  {enemy.parry_chance}")
        #print(f"Taunt-chance :  {enemy.taunt_chance}")
        #print(f"Stun-chance  :  {enemy.stun_chance}")
        print(f"__________________________ \n")
        print("Status effects:")
        if enemy.stun == True:
            print(f"Stuned       :  Yes")
        else:
            print(f"Stuned       :  No")
        if enemy.bleeding == True:
            print(f"bleeding     :  Yes")
            print(f"bleeding-counter :  {enemy.bleeding_counter}")
        else:
            print(f"bleeding     :  No")

        print("\n[z] Go back")
        go_back = input("> ")
        if go_back.lower() == "z":
            os.system("cls")
            return

def show_stats(player, enemy):
    while True:
    # print enemy or player stats  
        os.system("cls")
        print("___________________ \n")
        print("[x] See MY stats")
        print("[y] See ENEMY stats")
        print("[z] Go back")
        print("___________________")
        aceptable_answers = ["x", "y", "z"]
        answer = input("> ")

        if answer in aceptable_answers:
            os.system("cls")
            if answer.lower() == "x":
                show_player_stats(player)
            elif answer.lower() == "y":
                show_enemy_stats(enemy)
            elif answer.lower() == "z":
                os.system("cls")
                return        
###########################
def flamboyent_fling(player, enemy):
    # Kollar om slaget träffar med player.hit_chance
    os.system("cls")
    hit_chance = player.hit_chance // 5
    if hit_chance < 1:
        hit_chance = 1
    if random.randint(1, 100) <= hit_chance:
        # hit
        damage = player.power
        damage += damage * 2
        enemy.health -= damage
        print(f"Your flamboyant fling hits for {damage} damage!")
        print(f"Enemy health  :  {enemy.health}/{enemy.max_health}")
        pass
    else:
        # not hit
        print(f"Your strike misses and the enemy laughs.")
        print(f"Enemy health  :  {enemy.health}/{enemy.max_health}")
    
    print("\n\nType anything to continue.")
    input("> ")
    os.system("cls")
    return

def sneaky_stabb(player, enemy):
    # Kollar om slaget träffar med player.hit_chance
    os.system("cls")
    if random.randint(1, 100) <= player.hit_chance + 20:
        # hit
        damage = player.power
        if random.randint(1, 100) <= player.crit_chance:
            damage += damage
        damage = damage - enemy.defence
        if damage < 1:
            damage = 1
        enemy.health -= damage
        if random.randint(1, 100) <= player.stun_chance:
            enemy.stun = True
        if enemy.stun == True:
            print(f"Your strike hits for {damage} damage and stuns the enemy!")
        print(f"Your strike hits for {damage} damage!")
        pass
    else:
        # not hit
        print(f"Your strike misses and the enemy laughs.")
    print(f"Enemy health  :  {enemy.health}/{enemy.max_health}")

    print("\n\nType anything to continue.")
    input("> ")
    os.system("cls")
    return

def heavy_headbutt(player, enemy):
    # Kollar om slaget träffar med player.hit_chance
    os.system("cls")
    if random.randint(1, 100) <= player.hit_chance:
        # hit
        damage = player.power // 2
        if random.randint(1, 100) <= player.crit_chance:
            damage += damage
            enemy.stun = True
        damage = damage - enemy.defence
        if damage < 1:
            damage = 1
        enemy.health -= damage
        if random.randint(1, 100) <= player.stun_chance:
            enemy.stun = True
        if enemy.stun == True:
            print(f"Your headbutt hits for {damage} damage and stuns the enemy!")
        else:
            print(f"Your headbutt hits for {damage} damage!")
        pass
    else:
        # not hit
        print(f"Your headbutt misses and the enemy laughs.")

    print(f"Enemy health  :  {enemy.health}/{enemy.max_health}")
    print("\n\nType anything to continue.")
    input("> ")
    os.system("cls")
    return

def player_attack(player, enemy, confirmed_answer):
    while True:
        os.system("cls")
        print("This is your moveset:")
        print("___________________ \n")
        print("[x] Flamboyent fling")
        print("[y] Sneaky stabb")
        print("[c] Heavy headbutt")
        print("[z] Go back")
        print("___________________")
        aceptable_answers = ["x", "y", "c", "z"]
        answer = input("> ")

        if answer in aceptable_answers:
            if answer.lower() == "x":
                flamboyent_fling(player, enemy)
            elif answer.lower() == "y":
                sneaky_stabb(player, enemy)
            elif answer.lower() == "c":
                heavy_headbutt(player, enemy)
            elif answer.lower() == "z":
                os.system("cls")
                return
            if enemy.health <= 0:
                player.points += enemy.point_gain
                print(f"{enemy.name} has been slain, granting you {enemy.point_gain} points.\n\n")
                print("Type anything to continue.")
                input("> ")

            confirmed_answer = True
            return confirmed_answer
        else:
            pass
       
##########################
def player_defend(player, enemy, confirmed_answer):
    while True:
        os.system("cls")
        print("This is your defensive moveset:")
        print("___________________ \n")
        print("[x] Ciggarette")
        print("[y] Fruity flight")
        print("[z] Go back")
        print("___________________")
        aceptable_answers = ["x", "y", "z"]
        answer = input("> ")

        if answer in aceptable_answers:
            os.system("cls")
            if answer.lower() == "x":
                heal = 2
                player.heal(heal)
                print(f"You enjoy a smoke and recover {heal} hp.")
                print(f"Your hp  : {player.health}/{player.max_health}")
            elif answer.lower() == "y":
                if player.fled == False:
                    player.points = player.points // 2
                    enemy.health = 0
                    player.fled = True
                    print(f"You make a run in your high heels, dropping half of your points but outrunning {enemy.name}.")
                    print(f"Current points  : {player.points}")
                    print("This wont work twise...")
                else:
                    player.health = 0
                    print("You try running away, breaking your ankles and falling flat.")
                    input("> ")
                    game_over(player)
            elif answer.lower() == "z":
                os.system("cls")
                return

            print("\n\n[x] Move on")
            input("> ")
            os.system("cls")
            confirmed_answer = True
            return confirmed_answer
        else:
            pass

def player_turn(player, enemy, confirmed_answer):
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
                if player_attack(player, enemy, confirmed_answer) == True:
                    return confirmed_answer
            elif answer.lower() == "y":
                if player_defend(player, enemy, confirmed_answer) == True:
                    return confirmed_answer
            
            if answer.lower() == "z":
                show_stats(player, enemy)
        else:
            pass

###########################
def enemy_turn(player, enemy):

    special_chance = 25 

    if enemy.stun == False:
        if random.randint(1, 100) <= enemy.hit_chance:
            # Specialattack
            if random.randint(1, 100) <= special_chance:
                if enemy.variant == "common":
                    if random.randint(1, 100) <= 80:
                        enemy.heal(5)
                        print(f"{enemy.name} preformed a special move, healing 5 hp.")
                        print(f"Enemy health  : {enemy.health}/{enemy.max_health}")
                    else:
                        enemy.defence += 1
                        enemy.heal(2)
                        print(f"{enemy.name} preformed a special move, healing 2 hp and gaining 1 defence.")
                        print(f"Enemy health  : {enemy.health}/{enemy.max_health}")

                elif enemy.variant == "strange":
                    if random.randint(1, 100) <= 50:
                        damage = enemy.health // 2
                        damage -= player.defence
                        player.health -= damage
                        print(f"{enemy.name} preformed a special attack, dealing half of its current health as damage to you.")
                        print(f"You suffer {damage} damage.")
                    else:
                        damage = player.health // 2
                        player.health -= damage
                        print(f"{enemy.name} preformed a special attack, cutting your current health in half.")
                        print(f"You suffer {damage} damage.")

                elif enemy.variant == "legendary":
                    if random.randint(1, 100) <= 60:
                        #player.stun = True
                        #player.bleeding = True
                        player.defence -= 1
                        player.power -= 1
                        player.max_health -= 1
                        print(f"{enemy.name} preformed a legendary attack, permanently weakening you.")
                        print(f"You suffer -1 power, -1 max health, -1 defence.")
                        
                    else:
                        damage = enemy.power
                        player.health -= damage
                        print(f"{enemy.name} hits you for {damage} damage, ignoring your armour.")

            # Normal attack
            else:
                damage = enemy.power
                if random.randint(1, 100) <= enemy.crit_chance:
                    damage = enemy.power * 2
                damage -= player.defence
                player.health -= damage
                print(f"{enemy.name} hits you for {damage} damage!")
        else:
            print("The enemy misses, it's your time to laugh.")

        print(f"Your hp  : {player.health}/{player.max_health}")
        print("\n\nType anything to continue.")
        input("> ")
        if player.health <= 0:
            game_over(player)
               
    else:
        print("The enemy is stunned and has no interest in fighting you this round.")
        enemy.stun = False
        print("\n\nType anything to continue.")
        input("> ")

def fight(player, enemy):
    while True:
        confirmed_answer = False
        player_turn(player, enemy, confirmed_answer)
        os.system("cls")
        if enemy.health <= 0:
            os.system("cls")
            return
        enemy_turn(player, enemy)
        os.system("cls")

###########################

def game_over(player : Player):
    while True:
        os.system("cls")
        if player.points == 0:
            print("You died a faliure.")
        elif player.points > 10:
            print("You died kind of a faliure.")
        elif player.points > 50:
            print("You died.")
        elif player.points > 100:
            print("You died you fabulouus bastard.")
        print(f"This was your score  : {player.points}\n\n")
        print("Go again?")
        print("[x] Yes")
        print("[z] No")
        player_input = input("> ")
        if player_input.lower() == "x":
            main()
        elif player_input.lower() == "z":
            os.system("cls")
            quit()
        else:
            pass

# main
def main():
    while True:
        playing = start_game()
        if playing == True:
            break
    
    # Skapa spelkaraktären och namnge den 
    player_power = 3
    player_health = 1
    player_defence = 1
    hit_chance = 70
    parry_chance = 50
    taunt_chance = 50
    player = Player(choose_name(), player_power, hit_chance, parry_chance, taunt_chance, player_health, player_defence)

    first_room(player)

    # Main game loop lol
    lvl = 1
    while True:
        enemy = spawn_enemy(lvl)
        fight(player, enemy)
        choose_boon(player)
        if player.health <=0:
            game_over(player)
        lvl += 1
if __name__ == "__main__":
    main()