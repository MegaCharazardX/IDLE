from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import string
import random
from prettytable import PrettyTable

class PuzzleApp(App):
    def build(self):
        self.layout = GridLayout(cols=1, padding=10)

        self.label = Label(text="Enter the grid order (e.g., 7):")
        self.layout.add_widget(self.label)

        self.order_input = TextInput(multiline=False, input_filter="int")
        self.layout.add_widget(self.order_input)

        self.label_words = Label(text="Enter words (comma-separated):")
        self.layout.add_widget(self.label_words)

        self.words_input = TextInput(multiline=False)
        self.layout.add_widget(self.words_input)

        self.generate_button = Button(text="Generate Puzzle")
        self.generate_button.bind(on_press=self.generate_puzzle)
        self.layout.add_widget(self.generate_button)

        self.output_label = Label(text="")
        self.layout.add_widget(self.output_label)

        return self.layout

    def generate_puzzle(self, instance):
        try:
            order = int(self.order_input.text)
            words = self.words_input.text.split(',')
            root = Puzzle(order=order, words=words)
            self.output_label.text = f"Puzzle:\n{root}\nWords to Find: {', '.join(words)}"
        except Exception as e:
            self.output_label.text = f"Error: {str(e)}"


class Puzzle:
    def __init__(self, order=7, words=[]):
        self.order = order
        self.words = words
        self.Formated_words = []
        self.puzzle = PrettyTable()
        self.puzzle.border = False
        self.puzzle.header = False
        self.Validate()
        self.Create_Puzzle()

    def Validate(self):
        if len(self.words) >= self.order:
            raise ValueError(f"Number of words must be less than the order {self.order}")

        for i in self.words:
            if len(i) > self.order:
                raise ValueError(f"Number of characters in {i} are greater than the order {self.order}")
            if not i.isalpha():
                raise ValueError(f"Invalid characters in {i}")
            else:
                self.Formated_words.append(i.upper())

    def Create_Puzzle(self):
        self.grid = [['' for _ in range(self.order)] for _ in range(self.order)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for word in self.Formated_words:
            placed = False
            while not placed:
                row = random.randint(0, self.order - 1)
                col = random.randint(0, self.order - 1)
                direction = random.choice(directions)
                if self.can_place_word(word, row, col, direction):
                    self.place_word(word, row, col, direction)
                    placed = True

        Upper = string.ascii_uppercase
        for row in range(self.order):
            for col in range(self.order):
                if not self.grid[row][col]:
                    self.grid[row][col] = random.choice(Upper)

        for row in self.grid:
            self.puzzle.add_row(row)

    def can_place_word(self, word, row, col, direction):
        dr, dc = direction
        for i in range(len(word)):
            r, c = row + dr * i, col + dc * i
            if r < 0 or r >= self.order or c < 0 or c >= self.order:
                return False
            if self.grid[r][c] not in ('', word[i]):
                return False
        return True

    def place_word(self, word, row, col, direction):
        dr, dc = direction
        for i in range(len(word)):
            r, c = row + dr * i, col + dc * i
            self.grid[r][c] = word[i]

    def __repr__(self):
        return str(self.puzzle)
    
PuzzleApp().run()