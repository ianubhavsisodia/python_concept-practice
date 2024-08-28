#number guessing game
print("Welcome to number guessing game!\n""I have assigned a number between 1 to 100 and you have to guess it and you have only 9 chances.")
n = 18
number_of_guesses = 1
while(number_of_guesses<=9):
    ask = int(input("Guess the correct number\n"))
    if ask==n:
        print("Bingo, this is correct answer!!!\n","You took", number_of_guesses,"guess")
        break
    if 5<=ask<=15:
        print("Sorry, you need to guess a greater number\n")
    elif 23<=ask<=35:
        print("Try with lesser number\n")
    elif ask>=35:
        print("Sorry try lesser number!!\n")
    elif ask<=5:
        print("Try a greater number\n")
    elif 15<=ask<18:
        print("try a little greater number\n")
    elif 18<ask<=22:
        print("try a little lesser number")
        
    print(9-number_of_guesses,"no. of guesses left\n")
    number_of_guesses = number_of_guesses + 1
if number_of_guesses>9:
    print("Game over")
    

    