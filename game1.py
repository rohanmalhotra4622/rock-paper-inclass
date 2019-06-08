# game.py
import random

#def my_message():
#    return "Hello"
### if this script is executed from the command line

#def determine_winner(u , c):
#    return "rock"


#if __name__ == "__main__":
    

print("rock, paper, scissors, shoot!")
# Capture INPUTS
user_choice = input('Please choose one of the following:rock,paper,scissors:')

print("You chose:" , user_choice)

# Validate INPUTS
options = ['rock', 'paper', 'scissors']
if user_choice not in options :
    print("Invalid, Please try again")
    exit()
# generate Computer Selection
#print('Generating.....')
computer_choice = random.choice(options)
print("COMPUTER CHOICE:", computer_choice)

# Determine the winner
# rock beats scissors
# paper beats rock
# scissors beats paper
# same selection is a tie
if user_choice == computer_choice:
    print('Tie')
elif user_choice == 'rock' and computer_choice == 'paper':
    print('Winner is Paper')
    print('Computer Wins!')
elif user_choice == 'rock' and computer_choice == 'scissors':  
    print("Winner is Rock") 
    print('You Win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('Winner is Paper')
    print('You Win!')
elif user_choice == 'paper' and computer_choice == 'scissors':  
    print("Winner is Scissors")
    print("Computer Wins!")
elif user_choice == 'scissors' and computer_choice == 'rock':
    print('Winner is Rock')
    print("Computer Wins!")
elif user_choice == 'scissors' and computer_choice == 'paper':  
    print("Winner is Scissors")
    print("You Win!")

# Display final outputs/outcomes


















