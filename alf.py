def sqrt (target):
    x = 1
    while True:
        oldx = x
        x = (x + target / x) / 2
        if oldx == x:
            break
    return x
target = int(input ("Ввести число: "))
result = sqrt(target)
print(f'Корень из {target} - {result}')
print(f'{result}^2 = {result * result}')
