def perfect_num(n):

    sum = 1
    i = 2

    while i*i <=n:
        if i%n == 0:
            sum = sum + i + n/i
        i += 1

    return(True if sum == n and n!= 1 else False)


print('below are all perfect number number in range 1000')

n =2

for n in range(1000):
    if perfect_num(n):
        print(n , "perfect number")




perfect_num(6)