sum = 0
while True:
    x = input("enter a number")
    if x == "":
        print("result: ", sum)
        break
    sum += int(x)

