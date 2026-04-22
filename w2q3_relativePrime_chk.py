# check whether two numbers are relatively prime
# Two numbers are relatively prime (co-prime) if their GCD is 1.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
if gcd == 1:
    print(a, "and", b, "are Relatively Prime numbers")
else:
    print(a, "and", b, "are NOT Relatively Prime numbers")
