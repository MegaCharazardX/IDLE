import random
choices = ["Rock", "Paper", "Sissor"]
while True :
    user_choice = input("Enter your choice: ")
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("You lose!", computer_choice, "covers", user_choice)              
        else:
            print("You win!", user_choice, "smashes", computer_choice)    
    elif user_choice == "Paper":
        if computer_choice == "Sissor":
            print("You lose!", computer_choice, "cut", user_choice)              
        else:
            print("You win!", user_choice, "covers", computer_choice)
    elif user_choice == "Sissor":     
        if computer_choice == "Rock":
            print("You lose...", computer_choice, "smashes", user_choice)              
        else:
            print("You win!", user_choice, "cut", computer_choice)
    else:
        print("Invalid input! Please enter rock, paper or sissor")
    user_choice = input("Do you want to play again? (y/n): ")
    
    if user_choice == "n":
        break
    
print("Thanks for playing") 
