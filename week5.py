results = {}
student_ids = set()
attempt_logs = []

while True:
    print("\n===== Result Menu =====")
    print("1. Add Result")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ").strip()
        score = int(input("Enter Score: "))

        student_ids.add(student_id)
        results[student_id] = score
        attempt_logs.append((student_id, score))

        print("Result stored successfully")

    elif choice == "2":
        print("\n===== Results =====")
        for sid, sc in results.items():
            print(f"{sid} -> {sc}")

        print("\nUnique Student IDs:", student_ids)

        print("\nAttempt Logs:")
        for log in attempt_logs:
            print(log)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
