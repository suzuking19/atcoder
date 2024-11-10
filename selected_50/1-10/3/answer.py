t = int(input())

def formula(x: int) -> int:
    return x**2 + 2*x + 3

total = formula(formula(formula(t)+ t) + formula(formula(t)))

print(total)