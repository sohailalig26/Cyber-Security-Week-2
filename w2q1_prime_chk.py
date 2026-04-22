num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is NOT a Prime Number")
else:
    flag = True
    for i in range(2, num//2):
        if num % i == 0:
            flag = False
            break
    if flag == True:
        print(num, "is a Prime Number")
    else:
        print(num, "is NOT a Prime Number")
