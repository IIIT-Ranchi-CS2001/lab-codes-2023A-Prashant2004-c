s1 = "Maha Bharat"

# 1. mAHA bHARAT
string1 = string1 = s1.swapcase()
print("1. " + string1)

first_word, second_word = s1.split(' ')

# 2. Bharat
string2 = second_word.capitalize()
print("2. " + string2)

# 3. BharatBharatBharat
string3 = second_word * 3
print("3. " + string3)

# 4. Mera Bharat
string4 = s1.replace("Maha", "Mera")
print("4. " + string4)

# 5. Mera Bharat Mahan
string5 = s1.replace("Maha", "Mera") + " Mahan"
print("5. " + string5)