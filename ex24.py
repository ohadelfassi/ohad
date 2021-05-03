n = int(input())
print('<table border="1">')
for i in range(1, n + 1):
    print('\t<tr>')
    for j in range(1, n + 1):
        print(f"\t\t<td>{i * j}</td>")
    print("\t</tr>")
print("</table>")

