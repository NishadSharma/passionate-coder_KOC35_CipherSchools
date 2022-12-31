import random
winningnum = 45
guesscount = 0
num = 0
while num != winningnum:
    print("Guess the number:")
    num = int(input())
    if(num > winningnum):
        print("Too high")
        guesscount += 1
    elif(num < winningnum):
        print("Too Low")
        guesscount += 1
    elif(num == winningnum):
        guesscount += 1
        num == winningnum
        print(f"You guessed it correct the number is {winningnum}, you guessed in {guesscount} tries")
    else:
        continue