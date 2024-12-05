
# Fibonacci series using while loop
n = int(input("Enter the number of terms: "))


a, b = 0, 1
i = 0

if n == 1:
    print(f"Fibonacci sequence up to {n}:")
    print(a)
else:
    print("Fibonacci sequence:")
    while i < n:
        print(a, end=" ")
        a, b = b, a + b
        i += 1

