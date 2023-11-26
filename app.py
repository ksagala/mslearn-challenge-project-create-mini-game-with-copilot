import random
# write 'hello world' to the console
print('hello world')
def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    # Get user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Validate user's choice
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Generate computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
        
play_game()
