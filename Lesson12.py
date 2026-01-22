print('not inverted Patterns')
for r in range(1, 6):
    for c in range(r):
        print('*', end=' ')
    print()

print('inverted Patterns')
for r in range(5, 0, -1):
    for c in range (r):
        print('*', end= ' ')
    print()
