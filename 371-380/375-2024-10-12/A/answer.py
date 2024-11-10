n = int(input())
s = input()

len_s = len(s)

total = 0

for i in range(len(s)-2):
    if s[i] == "#":
        if s[i+1] == ".":
            if s[i+2] =="#":
                total += 1

print(total)