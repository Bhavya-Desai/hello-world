#CRDGAME
for i in range(int(input())):
    c_points = m_points = 0
    for n in range(int(input())):
        c, m = tuple(map(int, input().split()))
        if len(str(c)) > 1:
            c = sum(int(digit) for digit in str(c))

        if len(str(m)) > 1:
            m = sum(int(digit) for digit in str(m))

        if c == m:
            c_points +=1
            m_points += 1

        elif c > m:
            c_points += 1

        else:
            m_points += 1

    if c_points > m_points:
        print(0, end = " ")
        print(c_points)

    elif m_points > c_points:
        print(1, end = " ")
        print(m_points)

    else:
        print(2, end = " ")
        print(c_points)
