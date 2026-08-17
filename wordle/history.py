import json
import os


class GameHistory:
    """Store completed Wordle games and calculate game statistics."""

    def __init__(self) ->None:
        self.games= []
        self.filename = "history.json"

        if os.path.exists(self.filename):
            with open(self.filename) as file:
                self.games = json.load(file)

    def save(self) ->None:
        with open(self.filename, "w") as file:
            json.dump(self.games,file)

    def record_game(self, won: bool, attempts: int, word: str) -> None:
        game = {"won":won,
         "attempts": attempts,
         "word": word}
        self.games.append(game)
        self.save()

    @property
    def total_games(self) ->int:
        return len(self.games)

    @property
    def total_wins(self) ->int:
        wins = 0
        for game in self.games:
            if game["won"]:
                wins +=1
        return wins

    @property
    def win_percentage(self) -> float:
        if self.total_games == 0:
            return 0
        return (self.total_wins/self.total_games)*100

    @property
    def current_streak(self) -> int:
        current_streak = 0
        for game in reversed(self.games):
            if game["won"]:
                current_streak += 1
            else:
                break
        return current_streak

    @property
    def best_streak(self) -> int:
        best_streak=0
        current_streak = 0
        for game in self.games:
            if game["won"]:
                current_streak += 1
            else:
                current_streak = 0
            best_streak = max(best_streak, current_streak)
            #if current_streak>best_streak: best_streak = current_streak
        return best_streak
            






    




