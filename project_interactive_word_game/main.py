import random
WORDS = ("Manchester", "Barcelona", "Paris Saint-Germain")

def start_game():
  choice_word: str = random.choice(WORDS)
  letter_list: list = [ letter if letter in (" ","-") else "_" for letter in choice_word ]

  return choice_word, letter_list

def board(word) -> str:
  print("="*20)
  print("Try to guess the word")
  print("="*20)

  for letter in word:
    print(letter, end="")

    
def check_win(choiced_word, guess_word):
  if choiced_word ==  "".join(guess_word).capitalize():
    return True
  return False 

choiced_word, guess_word = start_game()
def game():
  win = False
  board(guess_word)
  while not win:
    player_input = input("\nEnter with a letter: ")

    for pos, letter in enumerate(choiced_word):
      if letter.lower() == player_input.lower():
        guess_word[pos] = player_input
    
    win = check_win(choiced_word, guess_word)
    board(guess_word)

game()