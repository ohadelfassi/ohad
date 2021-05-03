# funny_reverse.py

def funny(s):
    s=s.lower()
    words=s.split()
    result=[]
    for i in words:
        result.append(i[::-1].title())
    return " ".join(result)

result = funny("Foo bar")
print(result)
assert result == "Oof Rab"

result = funny("The quick brown fox")
print(result)
assert result == "Eht Kciuq Nworb Xof"

print("OK")
