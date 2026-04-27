while True:
    print("\n===== Quiz Menu =====")
    print("1. Register Student")
    print("2. Attempt Quiz")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
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

    elif choice == "2":
        print("\nQuiz feature will be added in next stage.")

    elif choice == "3":
        print("\nExiting...")
        break

    else:
        print("\nInvalid Choice! Try again.")
