n = int(input())
coordinate = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([x, y])

max_length = 0

for i in range(n):
    x, y = coordinate[i][0], coordinate[i][1]
    for j in range(n):
        if i == j:
            continue
        
        temp_x, temp_y = coordinate[j][0], coordinate[j][1]
        
        length = (((x-temp_x)**2) + ((y-temp_y)**2))**0.5

        max_length = max(max_length, length)

print(max_length)