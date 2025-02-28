import random
from art import logo


def score_sum(score, hand):
    """Count score"""
    score = 0
    for i in hand:
        score += i
    if score == 21 and len(hand) == 2:
        score = 0
    return score


def ace(score, hand):
    """Select value of Ace"""
    if score > 21:
        i = 0
        for eleven in hand:
            if eleven == 11:
                hand[i] = 1
            i += 1
    return hand


def add(hand):
    """Draw a card"""
    hand.append(random.choice(cards))
    return hand


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Ask for a game and deal cards
def blackjack():
    should_continue = False
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":

        print(logo)
        should_continue = True
        user_hand = random.choices(cards, k=2)
        user_score = 0
        user_score = score_sum(user_score, user_hand)
        ace(user_score, user_hand)
        user_score = score_sum(user_score, user_hand)
        print(f"Your cards: {user_hand}, your current score: {user_score}")
        computer_hand = random.choices(cards, k=1)
        computer_score = 0
        computer_first_score = score_sum(computer_score, computer_hand)
        print(f"Computer's first card: {computer_first_score}")
        first = computer_first_score
        computer_score = first

        # Drawing cards and counting their values
        while should_continue:
            """User"""
            play = input("Type 'y' to get another card, type 'n' to pass: \n")
            if play == "y":
                should_continue = True
                add(user_hand)
                user_score = score_sum(user_score, user_hand)
                if 0 < computer_score < 16 and user_score > computer_score:
                    add(computer_hand)
                    computer_score = score_sum(computer_score, computer_hand)
                ace(user_score, user_hand)
                user_score = score_sum(user_score, user_hand)
                ace(computer_score, computer_hand)
                computer_score = score_sum(computer_score, computer_hand)
                print(f"Your current hand: {user_hand}, current score: {user_score}")
                print(f"Computer's first card: {computer_first_score}")

            else:
                """Computer"""
                should_continue = False
                # Computer risk level ;)
                while 0 < computer_score < 16:
                    add(computer_hand)
                    computer_score = score_sum(computer_score, computer_hand)
                    ace(computer_score, computer_hand)
                    computer_score = score_sum(computer_score, computer_hand)
            if user_score > 21:
                should_continue = False

        print(f"Your final hand: {user_hand}, final score: {user_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        # Result of the game
        if user_score > 21:
            print(" You went over. You lose 😭\n")
        elif computer_score > 21:
            print(" Opponent went over. You win 😁 \n")
        elif user_score + computer_score == 0 and len(computer_hand + user_hand) == 4:
            print(" It's a Blackjack Draw !!!  😱😱😱😱 \n")
        elif computer_score == 0 and len(computer_hand) == 2:
            print(" Lose, opponent has Blackjack 😱 \n")
        elif user_score == 0 and len(user_hand) == 2:
            print(" You have Blackjack!!! You win 😱😁 \n")
        elif user_score > computer_score:
            print("You win 😃\n")
        elif user_score == computer_score:
            print("Draw  🙃\n")
        else:
            print("You lose 😤\n")

        # recursion
        blackjack()


blackjack()
