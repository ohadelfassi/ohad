def paint(width, height, commands):
    canvas = [[" " for x in range(width)] for y in range(height)]
    for k in commands:
        for i in range(k['start'][1], k['size'][1]+k['start'][1]):
            for j in range(k['start'][0], k['size'][0]+k['start'][0]):
                canvas[i][j] = k['char']

    return canvas


a = paint(20, 20, [
    {'char': '1', 'start': (0, 0), 'size': (2, 3)},
    {'char': '#', 'start': (3, 5), 'size': (6, 8)},
    {'char': '*', 'start': (6, 7), 'size': (8, 4)},
    {'char': 'X', 'start': (4, 14), 'size': (10, 3)},
    {'char': '9', 'start': (10, 19), 'size': (10, 1)},
])

# simple printout:
# for line in a:
#    print "".join(line)

# add a nice border for fancy printout:
top_line = "-" * (len(a[0]) + 2)
s = "\n".join([top_line] + ["|{}|".format("".join(row)) for row in a] + [top_line])

print(s)

expected = """
----------------------
|11                  |
|11                  |
|11                  |
|                    |
|                    |
|   ######           |
|   ######           |
|   ###********      |
|   ###********      |
|   ###********      |
|   ###********      |
|   ######           |
|   ######           |
|                    |
|    XXXXXXXXXX      |
|    XXXXXXXXXX      |
|    XXXXXXXXXX      |
|                    |
|                    |
|          9999999999|
----------------------
""".strip()

assert expected == s, (s, expected)

print("OK")
