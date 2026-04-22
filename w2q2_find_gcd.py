def gcd(a, b):
    gcd_value = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i
    return gcd_value
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD of", x, "and", y, "is", gcd(x, y))
