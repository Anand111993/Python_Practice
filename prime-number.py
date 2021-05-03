def is_prime_num(n):

    i , j , flag = 0, 0, 0

    for i in range(1, n+1, 1):
        if (i == 1 or i == 0):
            continue

        flag = 1
        for j in range(2, ((i//2) + 1), 1):
            if (i%j == 0):
                flag = 0
                break

        if (flag == 1):
            print(i, end= ' ')

    

N = 10

is_prime_num(N)