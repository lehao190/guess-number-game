import random

max_attempts_num = 10
user_attempts_num = 0

# Generate random number for users to guess.
correct_guess_number = random.randint(1, 100)

# Repeat until the player guesses correctly.
while user_attempts_num < max_attempts_num:
  # Ask the player for their guess.
  user_guess_number = int(input("Guess a number between 1 and 100: "))

  # Compare the guess to the number.
  if user_guess_number == correct_guess_number:
    print("You guessed correctly!")
    break
  else:
    print("You guessed incorrectly.")

  # Provide feedback ("higher" or "lower").
  if user_guess_number < correct_guess_number:
    print("Your guess is lower than the correct number.")
  else:
    print("Your guess is higher than the correct number.")

  # Increment the number of attempts.
  user_attempts_num += 1

  # Check if the player has run out of attempts.
  if user_attempts_num == max_attempts_num:
    print("You have run out of attempts. The correct number was", correct_guess_number)
