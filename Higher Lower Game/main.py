import random
from art import logo, vs
from game_data import data


print(logo)
# Choosing A
A_person = random.choice(data)
A_score = A_person['follower_count']

points = 0
should_continue = True

# Play loop
while should_continue:
    print(f"Compare A: {A_person['name']}, {A_person['description']}, from {A_person['country']} ")
    print(vs)

    # Choosing B that can't be A
    B_person = random.choice(data)
    while B_person == A_person:
        B_person = random.choice(data)

    print(f"Against B: {B_person['name']}, {B_person['description']}, from {B_person['country']} ")
    B_score = B_person['follower_count']

    # Guessing which has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ")
    print(logo)

    # Conditions of continuing or ending the game
    if A_score > B_score and guess == "A" or A_score < B_score and guess == "B":
        points += 1
        print(f"You're right! Current score: {points}.")
    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        should_continue = False

    # Now B becomes A
    A_person = B_person
    A_score = A_score
