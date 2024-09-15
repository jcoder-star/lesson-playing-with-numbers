def gcd(a, b):
    # Function to calculate Greatest Common Divisor (GCD) using Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Function to calculate LCM using the formula: LCM(a, b) = abs(a*b) // GCD(a, b)
    return abs(a * b) // gcd(a, b)

# Take input from the user
num1 = int(input(" "))
num2 = int(input("24:"))

# Calculate and print the LCM
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")


