n = int(input())
for i in range(n):
    print(" " * (n - 1 - i) + "*" * i + "*" + "*" * i + " " * (n - 1 - i))
for j in range(n-1,-1,-1):
    print(" " * (n - 1 - j) + "*" * j + "*" + "*" * j + " " * (n - 1 - j))