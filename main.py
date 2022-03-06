import random

def guess_num() -> str:
  """
  Basic random number game where the player picks a random number from 1,10 and checks if he guessed the secret number.
  """
  guess = int(input("\nPlease Enter a number: "))
  random_num = random.randint(1, 10)

  try:
    """ 
    If the user enters a non-number, it will prompt the user to enter one.
    """
    if guess == random_num:
      print("Hey you guessed it!")
    else:
      print(f"Wrong number, it was: {random_num}! Try again!")
      guess_num()
  except ValueError:
    print("Enter a number from 1,10 damn it!")
    guess_num()
