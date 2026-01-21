print("=== GPA CALCULATOR ===")

grade_points = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

total_credit_units = 0
total_quality_points = 0

num_courses = int(input("Enter number of courses: "))

for i in range(num_courses):
    print(f"\nCourse {i + 1}")
    course_name = input("Enter course name: ")
    credit_unit = int(input("Enter credit unit: "))
    grade = input("Enter grade (A-F): ").upper()

    point = grade_points.get(grade, 0)
    quality_point = point * credit_unit

    total_credit_units += credit_unit
    total_quality_points += quality_point

gpa = total_quality_points / total_credit_units

print("\n=== GPA RESULT ===")
print("Total Credit Units:", total_credit_units)
print("Total Quality Points:", total_quality_points)
print("Your GPA is:", round(gpa, 2))