x1 = x2 = 1
print(x1)
print(x2)
while x2 + x1 < 10000:
    x3 = x1 + x2
    print(x3)
    x1 = x2
    x2 = x3
