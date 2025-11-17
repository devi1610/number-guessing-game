import random
def play_game(start,end):
    secret_number=random.randint(start,end)
    attempts = 0
    print(f"\n I have selected a number between {start} and {end}. Try to guess it!")

    while True:
        try:
            guess=int(input("guess the number:"))
            attempts += 1
            if guess < secret_number:
                print("Number you have guessed is less than the secret one!!Try again...")
            elif guess > secret_number:
                 print("Number you have guessed is more than the secret one!!Try again...")
            else:
                print(f"\n yay!!You guessed the number correctly in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input!please enter a valid number")

def main():
    print("Number Guessing Game")
    print("-" * 30)

    while True:
        try:
            start=int(input("enter start of the  range:"))
            end=int(input("enter the end of the range:"))
            if start >= end:
                print("starting range should be less than end.Try again..")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    while True:
        play_game(start,end)

        play_again=input("Do you wanna play again? (y/n): ").lower()
        if play_again != "y":
            print("\n Thankyou for playing! Come again:))....")
            break

if __name__ == "__main__":
    main()
    