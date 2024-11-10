numbers = list(map(int, input().split()))
english = 'abcdefghijklmnopqrstuvwxyz'
output = ""

for number in numbers:
    output += english[number-1]

print(output)