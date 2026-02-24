# Student Management System (CRUD) using Dictionary
students = {}
def insert_student():
    roll = int(input("Roll No (unique): "))
    if roll in students:
        print("❌ Roll number already exists.")
        return

    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")

    students[roll] = {"name": name, "age": age, "course": course}
    print("✅ Student added successfully.")

def update_student():
    roll = int(input("Enter roll no to update: "))
    if roll not in students:
        print("❌ Student not found.")
        return

    print("Leave blank to keep old value.")
    name = input(f"New Name ({students[roll]['name']}): ")
    age_str = input(f"New Age ({students[roll]['age']}): ")
    course = input(f"New Course ({students[roll]['course']}): ")

    if name.strip() != "":
        students[roll]["name"] = name
    if age_str.strip() != "":
        students[roll]["age"] = int(age_str)
    if course.strip() != "":
        students[roll]["course"] = course
    print("✅ Student updated successfully.")

def delete_student():
    roll = int(input("Enter roll no to delete: "))
    if roll in students:
        del students[roll]
        print("✅ Student deleted successfully.")
    else:
        print("❌ Student not found.")

def display_students():
    if not students:
        print("⚠️ No students to display.")
        return

    print("\n--- All Students ---")
    for roll, info in students.items():
        print(f"Roll: {roll} | Name: {info['name']} | Age: {info['age']} | Course: {info['course']}")

def search_student():
    roll = int(input("Enter roll no to search: "))
    if roll in students:
        info = students[roll]
        print(f"✅ Found: Roll: {roll} | Name: {info['name']} | Age: {info['age']} | Course: {info['course']}")
    else:
        print("❌ Student not found.")

def menu():
    while True:
        print("\n========== Student Management ==========")
        print("1. Insert Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Search Student")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            insert_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

menu()