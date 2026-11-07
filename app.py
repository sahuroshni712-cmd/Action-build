
def get_students():
    students = [
        {"id": 1, "name": "Rahul"},
        {"id": 2, "name": "Priya"},
        {"id": 3, "name": "Aman"}
    ]

    return students


def main():
    print("Student Management System version 2")

    students = get_students()

    for student in students:
        print(student["id"], student["name"])


if __name__ == "__main__":
    main()
