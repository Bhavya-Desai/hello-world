for n in range(int(input())):
    jumps = int(input())
    strings = list(map(int, input().split()))

    total = 0
    for i in range(len(strings)-1):
        diff = abs(strings[i] - strings[i+1]) - 1
        total += diff

    print(total)
