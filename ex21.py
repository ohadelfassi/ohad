n = int(input())
for i in range(n):
    print(" " * (n - 1 - i) + "*" * i + "*" + "*" * i + " " * (n - 1 - i))

