import random
from hangman_words import word_list
from hangman_art import logo,stages
chosen_word=random.choice(word_list)
#Testing code
print(logo)
end_of_game=False
lives=len(stages)-1
display=[]
word_length=len(chosen_word)
for letter in chosen_word:
  
  display+="_"

while not end_of_game:
  guess=input("Guess a letter :").lower()
  if guess in display:
    print("you have already guessed that")
  for position in range(word_length):
    letter=chosen_word[position]
    if guess==letter:
      display[position]=letter
  print(f"{' '.join(display)}")
  if "_"not in display:
    end_of_game=True
    print("you win")

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives-=1
    if(lives==0):
      end_of_game=True
      print("you loose")
      print(f"the word is {chosen_word}")
  print(stages[lives])
  

     
     
  
  
    

