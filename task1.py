a, b = map(int, input().split())

c = 1
while True:
    print(c, end='')
    c = 1 + (c + b - 2) % a
    if c == 1:
        break
print()