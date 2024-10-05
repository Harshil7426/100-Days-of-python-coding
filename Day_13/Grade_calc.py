test_name = input("Enter the name of the test: ")
max_score = float(input("Enter the maximum score: "))
points_received = float(input("Enter the points received: "))

# Calculate percentage
percentage = (points_received / max_score) * 100
rounded_percentage = round(percentage, 2)

# Determine letter grade
if rounded_percentage >= 90:
    letter_grade = "A+ 🎉"
    color = "\033[92m"  # Green
elif rounded_percentage >= 80:
    letter_grade = "A 🎊"
    color = "\033[92m"  # Green
elif rounded_percentage >= 70:
    letter_grade = "B 😊"
    color = "\033[93m"  # Yellow
elif rounded_percentage >= 60:
    letter_grade = "C 😐"
    color = "\033[93m"  # Yellow
elif rounded_percentage >= 50:
    letter_grade = "D 😔"
    color = "\033[91m"  # Red
else:
    letter_grade = "U 😢"
    color = "\033[91m"  # Red

print(f"{color}You scored {rounded_percentage}% and received a letter grade of {letter_grade}\033[0m")
