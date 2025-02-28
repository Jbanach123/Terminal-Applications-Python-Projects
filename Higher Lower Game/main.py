mport
random
from art import logo

# Zmienne globalne
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# sprawdzanie numeru
def checkout(guess, number, turns):
    if guess == number:
        print(f"Udało się! Odpowiedź to {number}")
    elif guess > number:
        print("Za duża liczba.")
        return turns - 1
    else:
        print("Za mała liczba.")
        return turns - 1


# Wybór poziomu
def difficulty():
    difficult = input("Wybierz poziom. Wpisz 'łatwy' lub 'trudny': ")
    if difficult == "łatwy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    number = random.randint(1, 100)
    print(logo)
    print("Witaj w grze zgadnij numer!")
    print("Myślę o liczbie od 1 do 100")
    # Pomoc
    # print(f"Pssst {number}")
    turns = difficulty()
    guess = 0
    while guess != number:
        print(f"Masz {turns} prób na odgadnięcie.")
        guess = int(input("Wybierz liczbę: \n"))
        turns = checkout(guess, number, turns)
        if turns == 0:
            print(f"Nie udało ci się. Był to umer {number}.")
            return
        if guess != number:
            print("Zgadnij jeszcze raz.")


game()