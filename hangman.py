import PySimpleGUI as sg

class Hangman:
    def __init__(self) -> None:
        self._window = sg.Window(
            title="Hangman",
            layout=[[]],
            finalize=True,
            margins=(100, 100),
        )
