def nachmanize(s:str):
    res =""
    for i in range(1,len(s)+1):
        if i == len(s):
            res += (s[0:i])
        else:
            res += (s[0:i]) + " "
    return res


result = nachmanize("abcd")
print(result)
assert result == "a ab abc abcd"

result = nachmanize("shalom")
print(result)
assert result == "s sh sha shal shalo shalom"

print("OK")