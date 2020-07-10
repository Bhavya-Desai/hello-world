#PTMSSNG
for t in range(int(input())):

    n = int(input())
    x_coords = dict()
    y_coords = dict()

    for i in range(4*n-1):
        x, y = tuple(map(int, input().split()))
        x_coords[x] = x_coords.get(x, 0) + 1
        y_coords[y] = y_coords.get(y, 0) + 1

    for key, value in x_coords.items():
        if value % 2 != 0:
            a = key
            break

    for key, value in y_coords.items():
        if value % 2 != 0:
            b = key
            break

    print(a, b)
