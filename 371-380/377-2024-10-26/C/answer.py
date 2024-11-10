N, M = map(int, input().split())

ng_position = []

for _ in range(M):
    x, y = map(int, input().split())
    ng_position.append((x, y))
    if x + 2 <= N and y + 1 <= N:ng_position.append((x+2, y+1))
    if x + 1 <= N and y + 2 <= N:ng_position.append((x+1, y+2))
    if x - 1 > 0 and y + 2 <= N:ng_position.append((x-1, y+2))
    if x - 2 > 0 and y + 1 <= N:ng_position.append((x-2, y+1))
    if x - 2 > 0 and y - 1 > 0:ng_position.append((x-2, y-1))
    if x - 1 > 0 and y - 2 > 0:ng_position.append((x-1, y-2))
    if x + 1 <= N and y - 2 > 0:ng_position.append((x+1, y-2))
    if x + 2 <= N and y - 1 > 0:ng_position.append((x+2, y-1))

ng_position_set = set(ng_position)

ans = N ** 2 - len(ng_position_set)

print(ans)