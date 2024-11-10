s = input()

output = ""

for i in range(len(s)):
    if s[i] == ".":
        continue
    output += s[i]

print(output)