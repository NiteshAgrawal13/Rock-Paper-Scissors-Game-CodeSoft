#ROCK PAPER SCISSORS
import random

def get_user_choice():
    print("\nChoose rock, paper, or scissors:")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors:")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

def play_again():
    print("\nDo you want to play again? (yes or no)")
    return input().lower().startswith('y')

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("\nYou chose", user_choice)
        print("The computer chose", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print("\nResult:", result)
        if not play_again():
            break