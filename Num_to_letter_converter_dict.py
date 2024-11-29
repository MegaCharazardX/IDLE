instruction = """ Python code for converting alphabets to number
--Instruction : --
1. For single digits add an '0'(zero) infront.
2. DO NOT seperate letters in the words.
3. Seperat words with 1 space."""



start = input("Hit ENTER to start.")
if start == "" :
    print(instruction)
    
    

def alphabet_to_number(char):
    """Convert a single alphabet character to a number with a leading zero if necessary."""
    if char.isalpha() and char.islower():
        number = ord(char) - ord('a') + 1
        return f"{number:02}"
    else:
        raise ValueError("Input must be a lowercase alphabet character")

def number_to_alphabet(number):
    """Convert a two-digit number string to the corresponding alphabet character."""
    number = int(number)
    if 1 <= number <= 26:
        char = chr(ord('a') + number - 1)
        return char
    else:
        raise ValueError("Number must be between 01 and 26")

# Example dictionaries
alphabet_dict = {'a': '01', 'b': '02', 'z': '26', 'h': '08'}
number_dict = {'01': 'a', '02': 'b', '26': 'z', '08': 'h'}

# Convert alphabet to number using dictionary
converted_numbers = {char: alphabet_to_number(char) for char in alphabet_dict}
print("Alphabet to Number:", converted_numbers)

# Convert number to alphabet using dictionary
converted_alphabets = {num: number_to_alphabet(num) for num in number_dict}
print("Number to Alphabet:", converted_alphabets)