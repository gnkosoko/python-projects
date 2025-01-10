# Names:
# Date:
# Pokemon Simulator

#Init
import random

#Global Variables
pokemon_level = 0
pokemon_name = "Bulbasaur"
day = 1

#Function

def draw_bulbasaur():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬜⬛⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜
⬜⬜⬛🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛🟦🟦🟦⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦⬜⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜⬜🟦🟦⬛🟦🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦🟦⬛🟥⬜🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")

def draw_ivysaur():
        print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻🏻⬛🟥⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛🏻🏻🏻⬛🟥⬛🏽🏽⬛⬜⬜⬜
⬜⬜⬜⬛⬜⬛🏽🏽⬛🏻🏻⬛🟥🟥⬛⬛⬛🟩⬛⬜⬜
⬜⬜⬛🟦⬛🟩🟩⬛⬛⬛🏻🟥🟥⬛🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬛🟦🟦⬛⬛🟩🟩🏽⬛⬛⬛⬛⬛⬛⬛🟩🟩⬛⬜
⬜⬜⬛🟦🏽🟦🟦⬛⬛⬛🟩🟩⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬜⬛🟦🟦🏽🏽🟦🟦🟦🟦⬛⬛⬛🟩🟩⬛🟩🟩⬛🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🏽🟦🟦🟦🟦⬛🟩⬛🟩⬛🟩⬛⬛
⬛⬛🟦🟦🟦🏽🏽🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛🟩🟩⬛
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🏽🟦⬛⬛⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🏽🟦🌫️⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦⬛🟥🟥⬜🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")


def draw_venusaur():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥🟨🟨⬛🟥🟨🟨🟥⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟥🟥🟥⬛⬛⬛🟥🟥🟨🟨🟥⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥🟥⬛⬛🟨🟨🟨⬛⬛⬛⬛🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥⬛⬛🟥🟥⬛⬛🟨🟨⬛🟥🟨⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟥🟨🟨🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟩⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛🟨🟨🟥🟥🟥⬛⬜⬜
⬜⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛🟥🟥🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬛⬜⬜
⬜⬜⬜⬛🟦⬛⬛🟩⬛🟩🟩⬛⬛⬛🟥🟥🟥⬛⬛⬛⬛⬛⬛🟩⬛⬛⬜
⬜⬜⬜⬛🟦🟦⬛⬛⬛🟩⬛⬛🟩🟩⬛⬛⬛🟩⬛🟩🟩🟩⬛⬛🟩🟩⬛
⬜⬜⬜⬛🟦🟦🟦🟦🟦⬛⬛⬛⬛🟩🟩⬛🟩⬛⬛🟩⬛🟩🟩⬛🟩⬛⬛
⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛🟦⬛⬛🟩⬛🟩⬛🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬛🟩⬛🟩⬛
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦⬛🟦🟦🟦⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦🟦🟦⬛🟦🟦🌫️⬛⬜⬜
⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛🟦⬛🟦⬛🟦🌫️⬛⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦🟦🟦⬛⬜⬛⬛⬜⬜⬜⬜
⬜⬛⬛🟦🟦🟦🟦🟦⬛⬜⬜🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜""")

def train():
    global pokemon_level
    ans = input("Would you like to start your training?: ")
    if ans == "yes":
        pokemon_level = pokemon_level + 1
        print("Your Pokemon level is " + str(pokemon_level))
        while True:
            ans2 = input("Train Again? ")
            if ans2 == "yes":
                pokemon_level = pokemon_level + 1
                print("Your Pokemon level is " + str(pokemon_level))
            if ans2 == "no":
                print("Okay, your pokemon level is " + str(pokemon_level))
                break
    elif ans == "no":
        print("Okay, your pokemon level is " + str(pokemon_level))
        day == day + 1
        print("You are now on day " + str(day))


def gym_battle():
    global pokemon_level
    print("Welcome to the battle field")
    print("Are you ready to begin your battle?")
    ans = input("Are you ready to begin your battle?: ")
    if ans == "yes":
        pokemon_level = pokemon_level + 1
        outcome = random.randint(1,2)
        if outcome == 1:
            print("Great Job you won your battle!")
            print("Okay, your pokemon level is " + str(pokemon_level))
        elif outcome == 2:
            print("Sorry you lost...")

def rest():
    print("It's time for a break")
    print("Check out your info.")
    if pokemon_level < 16:
        pokemon_name == "Bulbasaur"
        print("Your name is Bulbasaur")
        print("You're on level " + str(pokemon_level))
        print("You're on day " + str(day))
        draw_bulbasaur()
    elif pokemon_level >= 16 and pokemon_level < 32:
        pokemon_name == "Ivysaur"
        print("Your name is Ivysaur")
        print("You're on level " + str(pokemon_level))
        print("You're on day " + str(day))
        draw_ivysaur()
    elif pokemon_level >= 32:
        pokemon_name == "Venusaur"
        print("Your name is Venusaur")
        print("You're on level " + str(pokemon_level))
        print("You're on day " + str(day))
        draw_venusaur()

def evolve():
    print("Check to see if your pokemon is eligible to evolve")
    if pokemon_level >= 16 and pokemon_level < 32:
        pokemon_name == "Ivysaur"
        print("Level " + str(pokemon_level) + " " + "Ivysaur")
    elif pokemon_level >= 32:
        pokemon_name == "Venusaur"
        print("Level " + str(pokemon_level) + " " + "Venusaur")
#Main
print("Welcome to Pokemon Evolution")
while True:
    print("Choose an activity for Day: " + str(day))
    print("""
    1.Train
    2. Gym Battle
    3. Rest(Display Info)
    4. Quit
    """)
    activity = int(input("Activity for the day: "))
    if activity == 1:
        print("Welcome to the training quarters")
        print("Train your pokemon in order for it to level up.")
        train()
        evolve()
        day = day + 1
        print("You are now on day " + str(day))
    elif activity == 2:
        gym_battle()
        evolve()
        day = day + 1
        print("You are now on day " + str(day))
    elif activity == 3:
        rest()
        day = day + 1
        print("You are now on day " + str(day))
    elif activity == 4:
        print("Thanks for playing Pokemon Evolution!")
        break
        day = day + 1
        print("You are now on day " + str(day))

#draw_bulbasaur()
#draw_ivysaur()
#draw_venusaur()
