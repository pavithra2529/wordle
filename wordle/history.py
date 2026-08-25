import csv
import os


class GameHistory:
    """Store completed Wordle games and calculate game statistics."""

    def __init__(self) -> None:
        self.games = []
        self.filename = "history.csv"

        if os.path.exists(self.filename):
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    row["won"] = row["won"] == "True"
                    row["attempts"] = int(row["attempts"])
                    self.games.append(row)

    def record_game(self, won: bool, attempts: int, word: str) -> None:
        game = {
            "won": won,
            "attempts": attempts,
            "word": word
        }

        self.games.append(game)

        file_exists = os.path.exists(self.filename)

        with open(self.filename, "a", newline="") as file:
            fieldnames = ["won", "attempts", "word"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(game)

    @property
    def total_games(self) -> int:
        return len(self.games)

    @property
    def total_wins(self) -> int:
        wins = 0

        for game in self.games:
            if game["won"]:
                wins += 1

        return wins

    @property
    def win_percentage(self) -> float:
        if self.total_games == 0:
            return 0

        return round((self.total_wins / self.total_games) * 100, 2)

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
        best_streak = 0
        current_streak = 0

        for game in self.games:
            if game["won"]:
                current_streak += 1
            else:
                current_streak = 0

            best_streak = max(best_streak, current_streak)

        return best_streak