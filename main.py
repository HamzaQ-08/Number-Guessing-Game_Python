import random

def guess_number():
    print("Welcome to the guessing game!")
    print("\nFor quitting the game enter 'q' or '0' ")
    print("\nGuess the number between 1 to 100\n")

    com_number = random.randint(1, 100)
    user_count = 0

    while True:
      user_number = input("Enter an integer between 1 to 100: ")

      if user_number.lower() == 'q' or user_number == '0':
        print("\nYou quit the game")
        break

      try:
        number = int(user_number)
        user_count += 1

        if number > com_number:
          print("\nYour number is too high\n")

        elif number < com_number:
          print("\nYour number is too low\n")

        else:
          print(f"\nCongratulations! You guessed the correct number {com_number} in {user_count} attempts.")

          play_again = input("\nDo you want to play again [yes/no]? ").lower()

          if play_again == 'yes':
            guess_number()
          else:
            print("Thanks for playing!")
          break

      except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
  guess_number()
