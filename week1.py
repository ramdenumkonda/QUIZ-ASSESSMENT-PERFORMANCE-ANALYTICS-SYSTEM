print("===== Student Registration System =====")

student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
student_department = input("Enter Department/Class: ")

if student_id.strip() == "" or student_name.strip() == "" or student_department.strip() == "":
    print("\nError: All fields are required!")
else:
    print("\n===== Student Details =====")
    print(f"Student ID      : {student_id}")
    print(f"Student Name    : {student_name}")
    print(f"Department/Class: {student_department}")
    print("\nRegistration Successful!")
