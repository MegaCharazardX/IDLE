instruction = """ Python code for converting alphabets to number
--Instruction : --
1. For single digits add an '0'(zero) infront.
2. DO NOT seperate letters in the words.
3. Seperat words with 1 space."""


alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']



def alphabet_to_number(char):
    """Convert a single alphabet character to a number with a leading zero if necessary."""
    if char.isalpha() and char.isupper():
        number = ord(char) - ord('a') + 1
        return f"{number:02}"
    else:
        raise ValueError("Input must be a uppercase alphabet character")

print(alphabet_to_number("HELLO"))

# def number_to_alphabet(number):
#     """Convert a two-digit number string to the corresponding alphabet character."""
#     number = int(number)
#     if 1 <= number <= 26:
#         char = chr(ord('a') + number - 1)
#         return char
#     else:
#         raise ValueError("Number must be between 01 and 26")


# start = input("Hit ENTER to start.")
# if start == "" :
#     print(instruction)
    
#     #start = 
    
#     char = "HELLO "
    
#     # Example usage
#     alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     number_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

#     # Convert alphabet to number
#     converted_numbers = [alphabet_to_number(char) ]
#     print("Alphabet to Number:", converted_numbers)

#     # Convert number to alphabet
#     #converted_alphabets = [number_to_alphabet(num) for num in number_list]
#     #print("Number to Alphabet:", converted_alphabets)

