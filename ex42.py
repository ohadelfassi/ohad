# sentences.py
def word_lengths(s):
    x = []
    for i in s.split():
        x.append(len(i))
    return x


result = word_lengths("Contrary to popular belief Lorem Ipsum is not simply random text")
print("Result:", result)
assert result == [8, 2, 7, 6, 5, 5, 2, 3, 6, 6, 4]
print("OK")
