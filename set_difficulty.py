from turtle import Screen
MODEL = ["easy", "normal", "hard"]


class Setdifficulty:
    def __init__(self) -> None:
        screen = Screen()
        self.answer = screen.textinput(
            "CHOOSE DIFFICULTY", "EASY, NORMAL, HARD")

    def choose(self):

        if self.answer.lower() == MODEL[0].lower():
            return 0.5
        elif self.answer.lower() == MODEL[1].lower():
            return 0.3
        else:
            return 0.1
