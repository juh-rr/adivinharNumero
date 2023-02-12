from art import logo
from difficulty_setting import difficulty_setting
import random
correctAnswer = random.randint(1, 100)

print(logo)
print("Welcome to the number guessing game!")
difficulty = input("Choose a difficulty, type 'easy' or 'hard': ").lower()

while difficulty != "easy" and difficulty != "hard":
  difficulty = input("Please choose a valid difficulty, type 'easy' or 'hard': ").lower()

qtdTries = difficulty_setting(difficulty)

keepTrying = True
while keepTrying == True and qtdTries > 0:
  answer = int(input("Please guess a number between 1 and 100: "))
  if answer == correctAnswer:
    print(f"Congratulations! You guessed {correctAnswer} right!")
    keepTrying = False
  elif answer > correctAnswer:
     print("Too high!")
     print(f"You have {qtdTries-1} tries left.")
     qtdTries -= 1
  elif answer < correctAnswer:
    print("Too low!")
    print(f"You have {qtdTries-1} tries left.")
    qtdTries -= 1
if qtdTries == 0:
  print(f"You're out of tries! The correct answer was {correctAnswer}.")
