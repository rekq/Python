import random
import hangman_words
import hangman_art

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
lives = 6

print(hangman_art.logo)
print(f"Solution: {chosen_word}")

display = []
for letter in chosen_word:
  display += "_"
print(f"{' '.join(display)}")


while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You've already guessed {guess}")
    
  
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life. ")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")
      
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")

  print(hangman_art.stages[lives])