import random

def get_player_choice():
    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def generate_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'scissors' and computer_choice == 'paper') or
        (player_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'You win!'
    else:
        return 'Computer wins!'

def play_rock_paper_scissors():
    player_score = 0
    computer_score = 0
    rounds_to_win = 3

    while player_score < rounds_to_win and computer_score < rounds_to_win:
        player_choice = get_player_choice()
        computer_choice = generate_computer_choice()

        print(f'You chose {player_choice}.')
        print(f'Computer chose {computer_choice}.')

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if 'win' in result:
            player_score += 1
        elif 'Computer' in result:
            computer_score += 1

        print(f'Score - You: {player_score}, Computer: {computer_score}\n')

    if player_score > computer_score:
        print('Congratulations! You won the game.')
    else:
        print('Sorry, the Computer won. Better luck next time!')

# Start the game
play_rock_paper_scissors()
