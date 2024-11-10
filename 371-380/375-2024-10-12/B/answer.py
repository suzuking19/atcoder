from decimal import Decimal

n = int(input())

px = py = 0

total_cost = 0

for _ in range(n):
    x, y= map(int, input().split())
    cost = (((px-x)**2) + ((py-y)**2))**0.5
    total_cost += cost
    px, py = x, y


print(total_cost)

