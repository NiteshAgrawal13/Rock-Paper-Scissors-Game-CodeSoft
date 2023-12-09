import random
def get_user_choice():
    print("\nChoose one in (rock, paper, or scissors):")
    choice1 = input().lower()
    while choice1 not in ["rock", "paper", "scissors"]:
        print("Invalid choice. please choose rock, paper, or scissors")
        choice1=input().lower()
    return choice1

def get_computer_choice():
    choice2 = ["rock", "paper", "scissors"]
    return random.choice(choice2)

def get_display_winner(user_choose, computer_choose):
    if user_choose== computer_choose:
        return 'It\'s a tie!'
    elif (user_choose == "rock" and computer_choose == "paper") or \
         (user_choose == "paper" and computer_choose == "scissors") or \
         (user_choose == "scissors" and computer_choose == "rock"):
        return "YOU WIN!"
    else:
        return "YOU LOSE!"

def play_again():
    print("\nIf you want to play again? then choose one (yes or no)")
    return input().lower().startswith('y')

if __name__ == "__main__":
    print("Welcome! to (ROCK, PAPAER, SCISSORS) Game")
    while True:
        user_choose = get_user_choice()
        computer_choose = get_computer_choice()
        print("\nYou chose a",user_choose)
        print("\nComputer chose a",computer_choose)
        result = get_display_winner(user_choose, computer_choose)
        print("\nResult is:",result)
        if not play_again():
            break

