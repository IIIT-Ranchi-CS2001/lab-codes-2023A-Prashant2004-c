
# characters present in a string are alphanumeric

string = input("Enter a string: ")

for char in string:
    if not char.isalnum():
        print(False)
        break
else:
    print(True)

