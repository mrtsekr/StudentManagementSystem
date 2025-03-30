import datetime

class Student:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__sex = sex
        self.__country_of_birth = country_of_birth

    def get_student_number(self): return self.__student_number
    def get_first_name(self): return self.__first_name
    def get_last_name(self): return self.__last_name
    def get_date_of_birth(self): return self.__date_of_birth
    def get_sex(self): return self.__sex
    def get_country_of_birth(self): return self.__country_of_birth
    def set_student_number(self, student_number): self.__student_number = student_number
    def set_first_name(self, first_name): self.__first_name = first_name
    def set_last_name(self, last_name): self.__last_name = last_name
    def set_date_of_birth(self, date_of_birth): self.__date_of_birth = date_of_birth
    def set_sex(self, sex): self.__sex = sex
    def set_country_of_birth(self, country_of_birth): self.__country_of_birth = country_of_birth

    def calculate_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.__date_of_birth, "%Y-%m-%d").date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

def write_to_file(students, filename="students.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            if student is not None:
                file.write(
                    f"{student.get_student_number()},{student.get_first_name()},"
                    f"{student.get_last_name()},{student.get_date_of_birth()},"
                    f"{student.get_sex()},{student.get_country_of_birth()}\n"
                )

def read_from_file(filename="students.txt"):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if len(students) >= 100:
                    break
                data = line.strip().split(",")
                if len(data) == 6:
                    student = Student(data[0], data[1], data[2], data[3], data[4], data[5])
                    students.append(student)
    except FileNotFoundError:
        print("File not found. No data loaded.")
    return students

def add_student(students):
    for i in range(len(students)):
        if students[i] is None:
            student_number = input("Enter student number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            sex = input("Enter sex: ")
            country_of_birth = input("Enter country of birth: ")
            students[i] = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
            print("Student added successfully.")
            return
    print("Student array is full.")

def find_student(students):
    student_number = input("Enter student number to find: ")
    for student in students:
        if student and student.get_student_number() == student_number:
            print(f"Student Number: {student.get_student_number()}")
            print(f"First Name: {student.get_first_name()}")
            print(f"Last Name: {student.get_last_name()}")
            print(f"Date of Birth: {student.get_date_of_birth()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of Birth: {student.get_country_of_birth()}")
            print(f"Age: {student.calculate_age()}")
            return
    print("Student not found.")

def show_all_students(students):
    for student in students:
        if student:
            print(f"Student Number: {student.get_student_number()}")
            print(f"First Name: {student.get_first_name()}")
            print(f"Last Name: {student.get_last_name()}")
            print(f"Date of Birth: {student.get_date_of_birth()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of Birth: {student.get_country_of_birth()}")
            print(f"Age: {student.calculate_age()}")
            print("-" * 20)

def show_students_by_year(students):
    year = input("Enter birth year to search: ")
    for student in students:
        if student and student.get_date_of_birth().startswith(year):
            print(f"Student Number: {student.get_student_number()}")
            print(f"First Name: {student.get_first_name()}")
            print(f"Last Name: {student.get_last_name()}")
            print(f"Date of Birth: {student.get_date_of_birth()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of Birth: {student.get_country_of_birth()}")
            print(f"Age: {student.calculate_age()}")
            print("-" * 20)

def modify_student(students):
    student_number = input("Enter student number to modify: ")
    for i in range(len(students)):
        student = students[i]
        if student and student.get_student_number() == student_number:
            print("Which field do you want to modify?")
            print("1. First Name")
            print("2. Last Name")
            print("3. Date of Birth")
            print("4. Sex")
            print("5. Country of Birth")
            choice = input("Enter your choice: ")
            if choice == "1":
                student.set_first_name(input("Enter new first name: "))
            elif choice == "2":
                student.set_last_name(input("Enter new last name: "))
            elif choice == "3":
                student.set_date_of_birth(input("Enter new date of birth (YYYY-MM-DD): "))
            elif choice == "4":
                student.set_sex(input("Enter new sex: "))
            elif choice == "5":
                student.set_country_of_birth(input("Enter new country of birth: "))
            else:
                print("Invalid choice.")
            print("Student record updated successfully.")
            return
    print("Student not found.")

def delete_student(students):
    student_number = input("Enter student number to delete: ")
    for i in range(len(students)):
        if students[i] and students[i].get_student_number() == student_number:
            students[i] = None
            print("Student deleted successfully.")
            return
    print("Student not found.")

def main():
    students = [None] * 100
    while True:
        print("\nMenu:")
        print("1. Write students to file")
        print("2. Read students from file")
        print("3. Add new student")
        print("4. Find student by number")
        print("5. Show all students")
        print("6. Show students by birth year")
        print("7. Modify student record")
        print("8. Delete student")
        print("9. Quit")
        choice = input("Enter choice (1-9): ").strip()
        if choice == "1":
            write_to_file(students)
        elif choice == "2":
            loaded = read_from_file()
            for i in range(min(len(loaded), 100)):
                students[i] = loaded[i]
            for i in range(len(loaded), 100):
                students[i] = None
        elif choice == "3":
            add_student(students)
        elif choice == "4":
            find_student(students)
        elif choice == "5":
            show_all_students(students)
        elif choice == "6":
            show_students_by_year(students)
        elif choice == "7":
            modify_student(students)
        elif choice == "8":
            delete_student(students)
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter 1-9.")

if __name__ == "__main__":
    main()
