import random

from game import Game
from history import GameHistory

words = []

with open("words.txt") as word: 
    for i in word: 
        clean_word = i.strip().lower()
        if len(clean_word) != 5:
            raise ValueError(f"Invalid word: {clean_word}. ""Every word must be 5 letters.")

        words.append(clean_word)
        words.append(clean_word)


secret = random.choice(words)
print (secret)
game = Game(secret, words) 
history = GameHistory()

while not game.is_over:
    print(game)
    guess = input("Enter the word: ").lower()

    try:
        game.make_guess(guess)
    except ValueError as e:
        print(e)

if game.is_won:
    attempt= len(game.guesses)
    print(f"You got it in {attempt}/6!")
else:
    print(f"The word was {secret}")

history.record_game(game.is_won,len(game.guesses),secret)

print(f"Total games: {history.total_games}")
print(f"Total wins: {history.total_wins}")
print(f"Win percentage: {history.win_percentage}")
print(f"Current streak: {history.current_streak}")
print(f"Best streak: {history.best_streak}")
