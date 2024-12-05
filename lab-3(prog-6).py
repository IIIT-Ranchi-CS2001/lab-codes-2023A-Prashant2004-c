
# number of occurrences of a particular character present in the given string

string = input("Enter a string: ")
ch = input("Enter the character to find: ")

count = 0

for char in string:
    if char == ch:
        count += 1


print(f"The character '{ch}' appears {count} times in the string.")
