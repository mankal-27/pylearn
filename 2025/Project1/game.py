import random


def get_computer_choice():
    return random.choice(["snake", "water", "gun"])


def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "snake" and computer == "water") or \
            (player == "water" and computer == "gun") or \
            (player == "gun" and computer == "snake"):
        return "You win! 🎉"
    else:
        return "Computer wins! 😢"


def play_game():
    print("Welcome to Snake, Water, Gun Game! 🎮")
    choices = ["snake", "water", "gun"]

    player_choice = input("Enter your choice (snake/water/gun): ").strip().lower()
    if player_choice not in choices:
        print("Invalid choice! Please enter 'snake', 'water', or 'gun'.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)


# Run the game
play_game()
