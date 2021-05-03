num = int(input("enter the number "))

if num == 0 or num == 1:
    print(1) 

else:
    fact = 1
    while(num > 1):
        fact *= num
        num -= 1

    print(fact)

    




    
