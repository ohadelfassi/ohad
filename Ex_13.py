x=int(input("player 1 enter a number between 1 and 100"))
while True:
    y=int(input("player 2 guess a number between 1 and 100"))
    if y==x:
        print("Correct! You win!")
        break
    elif y>x:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")


