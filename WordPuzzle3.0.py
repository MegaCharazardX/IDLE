import string
import random, time
import sys
from prettytable import PrettyTable
import requests

app_id = "ec6c8650"
app_key = "6fa950ece3a3686a4b0995ba3c5d9b3e"
language = "en-gb"
word = "exam"
url = f"https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/{language}/{word.lower()}"

headers = {
    "app_id": app_id,
    "app_key": app_key
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}, {response.text}")

def tprint(word, interval = 0.015):
    for char in word:
        time.sleep(interval)
        #print(char, end = "")
    # print("\n")
        sys.stdout.write(char)
        sys.stdout.flush()
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
        #self.Export()
    
    def Validate(self):
        if len(self.words) >= self.order:
            raise ValueError(f"Number of words in {self.words} must be less than the order {self.order}")
        
        for i in self.words:
            if len(i) > self.order:
                raise ValueError(f"Number of characters in {i} are greater than the order {self.order}")
            if not i.isalpha():
                raise ValueError(f"Invalid characters in {i}")
            else:
                self.Formated_words.append(i.upper())
        
    def Create_Puzzle(self):
        self.grid = [['' for _ in range(self.order)] for _ in range(self.order)]

        directions = [
            (0, 1),   
            (0, -1),  
            (1, 0),   
            (-1, 0),  
            (1, 1),   
            (-1, -1), 
            (1, -1),  
            (-1, 1)   
        ]

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
    
    def Export(self, filename = "Puzzle"):
        #tprint(self)
        f = open(f"{filename}.txt", "w+")
        f.write(str(self))
        f.write("\n\n")
        f.write(str(self.words))
        f.close()
        tprint("Saved succesfully")

while True :
    def validateIsString(smthing):
        if smthing.isdigit():
            return True
        else:
            return False

    _order = input("Enter the order (number of rows) : ")
    if validateIsString(_order):
        _order = int(_order)
    else :
        tprint("!! Order Must Be An Integer !!")
        continue
    
    num_of_words = input("Enter the number of word (must be less than the order): ")
    
    if validateIsString(num_of_words):
        num_of_words = int(num_of_words)
    else :
        tprint("!! Order Must Be An Integer !!")
        continue
    if num_of_words >= _order:
        tprint("Must be less than the order")
        continue
    i = 1    
    words = []
    while i <= num_of_words :
        word = input(f"Enter word {i} : ")
        if word.isalpha():
            if word in words :
                tprint("Word already Entered, Try another word ")
                continue
            elif len(word) <= _order :
                i +=1
                words.append(word)
            else:
                tprint("Length of the word must be less than the order ")
                continue
        else:
            tprint("Word must not contain aby special caracters")
            continue
                
    root = Puzzle(order=_order, words = words)
    tprint(root)
    tprint(f"Words to be found : {words}")

    c = input("Enter C for going again, E for saving this puzzle, Q for quiting : ")
    
    if c in "cC":
        continue
    elif c in "eE":
        flname = input("Enter file Name : ")
        root.Export(filename=flname)
        c = input("Enter C for going again, Q for quiting : ")
        if c in "cC":
            continue
        elif c in "qQ":
            tprint("Thank u for playing")
            break
        else:
            tprint("Invalid choice")
    
    elif c in "qQ":
        tprint("Thank u for playing")
        break
    
    else:
        tprint("Invalid choice")
        
        
