name = str(input("enter name: "))
roll_no = int(input("enter roll number: "))
marks = int(input("enter marks: "))


print("Name:" + name)
print("Roll Number:" , roll_no)
print("Marks:" , marks)

if(marks >= 90) : 
# Grade_Point = 10
 print("Grade Point:" + "10")
# Remarks = "OUTSTANDING"
 print("Remark:" + "OUTSTANDING")

elif(marks >= 80 and marks < 90) : 
 print("Grade Point:" + "9")
 print("Remark:" + "VERY GOOD")

elif(marks >= 70 and marks < 80) : 
 print("Grade Point:" + "8")
 print("Remark:" + "GOOD")

elif(marks >= 60 and marks < 70) : 
 print("Grade Point:" + "7")
 print("Remark:" + "AVERAGE")

elif(marks >= 50 and marks < 60) : 
 print("Grade Point:" + "6")
 print("Remark:" + "PASS")

elif( marks < 50) : 
 print("Grade Point:" + "0")
 print("Remark:" + "FAIL")


    

