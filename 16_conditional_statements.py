# Conditional Statements

#Example: if statement

age = 18
if age >= 18:
    print("You are eligible to vote")


#Example: if-else

temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")


#Example: if-elif-else

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
