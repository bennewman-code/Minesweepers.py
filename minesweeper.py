import random

grid = ["A1", "A2", "B1", "B2"]

bomb = []
bomb.append(random.choice(grid))

print("""
A1 A2
B1 B2
""")

print("There's one bomb!")
print("Don't set it off")

def check_guess(guess):
    if guess in bomb:
        print("You chose a Bomb!")
        print("Game Over")
        exit(0)
    else:
        print(f"{guess} is safe")

first_guess_input = input("Choose which grid reference from above: ")
check_guess(first_guess_input)

second_guess_input = input("Choose the next grid reference from above: ")
check_guess(second_guess_input)

third_guess_input = input("Choose the last grid reference from above: ")
check_guess(third_guess_input)

print("You Win! You guessed right")
