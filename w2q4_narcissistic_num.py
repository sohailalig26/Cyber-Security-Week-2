# Function to display all n-digit narcissistic numbers

def narcissistic(n):
    start = 10 ** (n - 1)
    end = 10 ** n

    for num in range(start, end):
        temp = num
        sum = 0
        while temp > 0:
            digit = temp % 10
            sum = sum + (digit ** n)
            temp = temp // 10
        if sum == num:
            print(num)
n = int(input("Enter number of digits: "))
print("Narcissistic numbers are:")
narcissistic(n)
