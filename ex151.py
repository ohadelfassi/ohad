def median(data):
    x=sorted(data)
    if len(x) % 2 == 1:
        return x[len(x) // 2]
    return (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2
    # ------ YOUR CODE HERE -------
    # -----------------------------


result = median([10, 15, 20, -40, 90])
print(result)
assert result == 15

result = median([10, 15, 20, -40, 90, 33])
print(result)
assert result == 17.5

print("OK")
