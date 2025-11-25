Students = dict[str, list[int]]

def add_student(students: Students) -> None:
    """
    Add a new student to the dictionary if they do not already exist.

    This function prompts the user to enter a student's name and
    adds the student to the dictionary with an empty list of grades.
    """
    name: str = input("Enter student name: ").strip()
    if name in students:
        print("The specified student exists in the list")
    else:
        students[name] = []

def add_grades(students: Students) -> None:
    """
    Add grades for an existing student.

    The function asks for the student's name and then allows the user
    to enter multiple grades (0–100). The process ends when the user
    types 'done'.
    """
    name: str = input("Enter student name: ").strip()
    if name not in students:
        print('Student not found')
        return
    while True:
        grade: str = input("Enter a grade (or 'done' to finish): ").strip()
        if grade.lower() == 'done':
            break

        try:
            value = int(grade)
            if 0 <= value <= 100:
                students[name].append(value)
            else:
                print("The score must be between 0 and 100.")
        except ValueError:
            print("The grade must be an integer.")
def show_report(students: Students) -> None:
    """
    Display a report of all students and their average grades.

    For each student, the function calculates and prints their average grade.
    If a student has no grades, 'N/A' is shown instead.
    The function also prints the maximum, minimum, and overall average
    of all available averages.
    """
    print("--- Student Report ---")
    if not students:
        print('No students found')
        return

    averages: list[float] = []
    for name, grades in students.items():
        if grades:
            avg = round(sum(grades) / len(grades), 1)
            averages.append(avg)
            print(f"{name}'s average grade is {avg}.")
        else:
            print(f"{name}'s average grade is N/A.")

    if averages:
        print("-" * 10)
        print(f"Max Average: {max(averages)}")
        print(f"Min Average: {min(averages)}")
        print(f"Overall Average: {round(sum(averages) / len(averages), 1)}")

def find_top_performer(students: Students) -> None:
    """
    Find and display the student with the highest average grade.

    Only students who have at least one grade are considered.
    The function calculates each student's average and prints the
    name and the average of the top performer.
    """
    if not students:
        print('No students found')
        return

    valid_students = ((name, grades) for name, grades in students.items() if grades)
    best_student = max(valid_students, key = lambda x: sum(x[1]) / len(x[1]),
                       default = None)
    if best_student:
        name, grades = best_student
        print(f'The student with the highest average is {name} '
              f'with a grade of {round(sum(grades) / len(grades), 1)}.')
    else:
        print('The best student is absent because there are no grades.')


def main() -> None:
    """
    Run the main menu loop for the Student Grade Analyzer application.

    The function displays a menu, processes user input,
    and calls other functions depending on the selected option.
    """
    students: Students = {}
    menu = {
        '1': "1. Add a new student",
        '2': "2. Add a grades for a student",
        '3': "3. Show report (all students)",
        '4': "4. Find top performer",
        '5': "5. Exit"
    }

    while True:
        print('--- Student Grade Analyzer ---')
        print("\n".join(menu.values()))
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                add_student(students)
            case '2':
                add_grades(students)
            case '3':
                show_report(students)
            case '4':
                find_top_performer(students)
            case '5':
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Enter a number from 1 to 5.")

if __name__ == '__main__':
    main()