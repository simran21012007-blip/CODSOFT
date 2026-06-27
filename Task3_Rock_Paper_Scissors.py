import random

OPTIONS = ["rock", "paper", "scissors"]

def display_menu():
    print("\n" + "=" * 50)
    print("        ROCK PAPER SCISSORS GAME")
    print("=" * 50)
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    print("-" * 50)

def get_user_choice():
    while True:
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            return "rock"
        elif choice == "2":
            return "paper"
        elif choice == "3":
            return "scissors"
        elif choice == "4":
            return None
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


def get_computer_choice():
    return random.choice(OPTIONS)


def decide_winner(user, computer):
    if user == computer:
        return "Tie"

    if (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "User"

    return "Computer"


def display_round_result(user, computer, result):
    print("\n" + "-" * 40)
    print(f"You Selected      : {user.capitalize()}")
    print(f"Computer Selected : {computer.capitalize()}")

    if result == "Tie":
        print("Result            : Match Draw")
    elif result == "User":
        print("Result            : Congratulations! You won this round.")
    else:
        print("Result            : Computer won this round.")
    print("-" * 40)


def display_score(user_score, computer_score):
    print("\nCurrent Score")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")


def main():
    print("=" * 50)
    print("WELCOME TO ROCK PAPER SCISSORS")
    print("=" * 50)
    print("Rules:")
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beats Paper")
    print("-" * 50)
    
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        display_menu()

        user_choice = get_user_choice()

        if user_choice is None:
            break

        computer_choice = get_computer_choice()

        result = decide_winner(user_choice, computer_choice)

        display_round_result(user_choice, computer_choice, result)

        rounds += 1

        if result == "User":
            user_score += 1
        elif result == "Computer":
            computer_score += 1

        display_score(user_score, computer_score)

    print("\n" + "=" * 50)
    print("              GAME SUMMARY")
    print("=" * 50)
    print(f"Rounds Played : {rounds}")
    print(f"Your Score    : {user_score}")
    print(f"Computer Score: {computer_score}")
    if rounds > 0:
        win_percentage = (user_score / rounds) * 100
        print(f"Win Percentage : {win_percentage:.2f}%")
    else:
        print("Win percentage : 0.00%")
     
    if user_score > computer_score:
        print("\nOverall Winner: You")
    elif computer_score > user_score:
        print("\nOverall Winner: Computer")
    else:
        print("\nOverall Result: Draw")

    print("\nThank you for playing Rock Paper Scissors!")
    print("Have a great day!")
    print("=" * 50)


if __name__ == "__main__":
    main()