# Student Marks & Grade Automation System (Basic Version)

print("=== Student Result & Grade System ===")

name = input("Enter Student Name: ")

mark1 = float(input("Enter Mark 1: "))
mark2 = float(input("Enter Mark 2: "))
mark3 = float(input("Enter Mark 3: "))
mark4 = float(input("Enter Mark 4: "))
mark5 = float(input("Enter Mark 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5 
average = total / 5

# Grade Calculation
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n--- Result ---")
print("Student Name  :", name)
print("Total Marks   :", total)
print("Average       :", round(average, 2))
print("Grade         :", grade)