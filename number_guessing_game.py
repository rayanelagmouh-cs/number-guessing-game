
import random


def choose_difficulty():
    print("\nChoose your difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty = input("Enter 1, 2, or 3: ")

    if difficulty == "1":
        return 50
    elif difficulty == "2":
        return 100
    elif difficulty == "3":
        return 500
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
        return None


def play_game(max_number):
    number = random.randint(1, max_number)
    attempts = 0

    while True:
        try:
            guess = int(input("GUESS THE NUMBER: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if guess < 1 or guess > max_number:
            print("Please enter a number between 1 and", max_number)
            continue

        attempts += 1

        if guess > number:
            print("Too high! Try again")
        elif guess < number:
            print("Too low! Try again")
        else:
            print("Correct!")
            print("You got it in", attempts, "attempts!")
            break


def main():
    print("==============================")
    print("   NUMBER GUESSING GAME")
    print("==============================")

    while True:
        max_number = choose_difficulty()

        if max_number is None:
            continue

        print("I'm thinking of a number between 1 and", max_number)

        play_game(max_number)

        while True:
            play_again = input(
                "Do you want to play again? (yes/no): "
            ).strip().lower()

            if play_again == "yes":
                break
            elif play_again == "no":
                print("Thanks for playing!")
                return
            else:
                print("Please enter yes or no!")


if __name__ == "__main__":
    main()
