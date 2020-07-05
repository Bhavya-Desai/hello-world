for t in range(int(input())):
    k = int(input())
    temp = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if i == 1 and j == 1: print('O', end = "")
            else:
                if temp < k-1:
                    print('.', end = "")
                    temp += 1
                else:
                    print("X", end =  "")
        print()
