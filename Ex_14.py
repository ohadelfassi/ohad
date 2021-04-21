x=int(input("enter a number between 1 and 100"))
min=0
max=101
(min+max)//2
while True:
    print("Is your number",(min+max)//2)
    if x==(min+max)//2:
        print("y")
        break
    elif x>(min+max)//2:
        min=(min+max)//2
        print("n")
    else:
        max=(min+max)//2
        print("n")


