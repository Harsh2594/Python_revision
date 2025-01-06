import random
print("Welcome to number gusesing game:? ")
print("I'm thinking of a number between 1 to 100")
choice = input("choose a difficuly. Type 'easy' or 'hard': ")
def level(difficulty_level):
  random_number = random.randint(1,100)
  if difficulty_level == 'hard':
    attempt = 5
  else:
    attempt = 10
  while attempt > 0:
    guess_number = int(input("Make a guess-- "))
    if guess_number < random_number:
      print("Too low\nGuess again ")
    elif guess_number > random_number:
      print("Too high!\nGuess again")
    else:
      print("Exact Match\nYOU WIN!")
      break
    attempt = attempt-1
  else:
    print("Your attempt is over!\nYOU LOSS!!!!!!!!!!!")

level(choice)