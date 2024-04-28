from art import logo
from random import randint
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def easy_game_mode(computer_generated_num):
  """This Function stimulates the easy mode of the game"""
  user_attempts = 10
  print(f"You have {user_attempts} attempts remaining to guess the number.")
  while user_attempts <= 10:
    user_choosen_num = int(input("Make a guess : "))
    if user_choosen_num == computer_generated_num:
      print(f"You got it! The answer was {computer_generated_num}.")
      break
    elif user_choosen_num > computer_generated_num:
      print("Too high.","Guess again",end='\n')
      user_attempts -= 1
      print(f"You have {user_attempts} attempts remaining to guess the number.")
    elif user_choosen_num < computer_generated_num:
      print("Too low.","Guess again",end='\n')
      user_attempts -= 1
      print(f"You have {user_attempts} attempts remaining to guess the number.")
    if user_attempts == 0:
      print("You've run out of guesses, you lose.")
      break
      
def hard_game_mode(computer_generated_num):
  """This Function stimulates the hard mode of the game"""
  user_attempts = 5
  print(f"You have {user_attempts} attempts remaining to guess the number.")
  while user_attempts <= 10:
    user_choosen_num = int(input("Make a guess : "))
    if user_choosen_num == computer_generated_num:
      print(f"You got it! The answer was {computer_generated_num}.")
      break
    elif user_choosen_num > computer_generated_num:
      print("Too high.","Guess again",end='\n')
      user_attempts -= 1
      print(f"You have {user_attempts} attempts remaining to guess the number.")
    elif user_choosen_num < computer_generated_num:
      print("Too low.","Guess again",end='\n')
      user_attempts -= 1
      print(f"You have {user_attempts} attempts remaining to guess the number.")
    if user_attempts == 0:
      print("You've run out of guesses, you lose.")
      break
      

def start_the_game():
  """This function Starts the Game"""
  computer_generated_num = randint(1,100)
  print(f"Computer Generated Number : {computer_generated_num}")
  user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if user_choice == "easy":
    easy_game_mode(computer_generated_num)
  else:
    hard_game_mode(computer_generated_num)
start_the_game()


    
  