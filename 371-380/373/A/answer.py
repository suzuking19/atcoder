total = 0

for i in range(1, 13):
    s = input()
    if len(s) == i:
        total += 1

print(total)