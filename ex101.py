x = input()
if x != "":
    x = int(x)
    max = -9999999999999999999999
    min = 99999999999999999999999
    items = 0
    sum = 0
list_1 = []
while x != "":
    items += 1
    list_1.append(x)
    sum += x
    if x < min:
        min = x
    if x > max:
        max = x
    x = input()
    if x!="":
        x=int(x)
list_2=sorted(list_1)
print("Items: ", items)
print("Min: ", min)
print("Max: ", max)
print("Avg", float(sum) / items)
print("median: ", list_2[items // 2])
