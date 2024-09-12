

# sum of the digits of the given number using a while loop


num = int(input("Enter a number: "))

sum = 0
i = num

while i > 0:
    digit = i % 10
    sum += digit
    i //= 10  


print(f"The sum of the digits of the number {num} is {sum}")
