MAX_GUESSES = 6
WORD_LENGTH = 5


class GuessResult:
    """Represent the result of a single Wordle guess."""

    def __init__(self, guess: str, result: list[str]) -> None:
        self.guess = guess
        self.result = result

    def __str__(self) -> str:
        symbols = {
            "correct": "✓",
            "present": "~",
            "absent": "✗",
        }

        letters = "  ".join(self.guess.upper())
        marks = "  ".join(symbols[result] for result in self.result)

        return letters + "\n" + marks


def evaluate_guess(secret: str, guess: str) -> GuessResult:
    """Evaluate a guess against the secret word."""

    result = ["absent"] * WORD_LENGTH
    available_letters = list(secret)

    # First pass: correct letters
    for i in range(WORD_LENGTH):
        if secret[i] == guess[i]:
            result[i] = "correct"
            available_letters.remove(guess[i])

    # Second pass: present or absent letters
    for i in range(WORD_LENGTH):
        if result[i] == "correct":
            continue

        if guess[i] in available_letters:
            result[i] = "present"
            available_letters.remove(guess[i])
        else:
            result[i] = "absent"

    return GuessResult(guess, result)


class Game:
    """Manage a Wordle game and track player guesses."""

    def __init__(self, secret: str, words: list[str]) -> None:
        self.secret = secret
        self.words = words
        self.guesses: list[GuessResult] = []

    def make_guess(self, word: str) -> GuessResult:
        if self.is_over:
            raise ValueError("The game is already over.")

        if len(word) != WORD_LENGTH:
            raise ValueError("Guess must be a 5-letter word.")

        if word not in self.words:
            raise ValueError("The guess word is not in the word list.")

        result = evaluate_guess(self.secret, word)
        self.guesses.append(result)

        return result

    @property
    def is_won(self) -> bool:
        for result in self.guesses:
            if result.guess == self.secret:
                return True

        return False

    @property
    def is_over(self) -> bool:
        if self.is_won:
            return True

        return len(self.guesses) == MAX_GUESSES
           

    def __str__(self) -> str:
        lines = []

        for result in self.guesses:
            lines.append(str(result))

        remaining_attempts = MAX_GUESSES - len(self.guesses)
        lines.append(f"Remaining attempts: {remaining_attempts}")

        return "\n".join(lines)