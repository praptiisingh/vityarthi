from certifications_required import get_certification_marks
from assginment import assign_requirements
from vityarthi import completionornot
from viva import viva

if __name__ == '__main__':

    # 1. Get Initial Setup and Certification Marks (10 max)
    # The get_certification_marks function initializes name and reg_no globally,
    # and returns the mark.
    name, reg_no, marks_certification = get_certification_marks()

    # Initialize total marks with the certification mark
    total_marks = marks_certification

    # --- 2. Calculate Assignment Marks (10 max) ---
    print("\n--- Assignment Section (10 Marks) ---")
    try:
        assign = int(input("Enter the number of assignments (programmes) completed (e.g., 35):\n"))
        date1 = int(input("Enter the date of assignment completed in November 2025 (e.g., 20):\n"))
    except ValueError:
        print("Invalid numerical input. Assignment marks set to 0.")
        assign = 0
        date1 = 0

    marks_assignment = assign_requirements(assign, date1)
    total_marks += marks_assignment

    # --- 3. Calculate Viva Marks (5 max) ---
    print("\n--- Viva/Quiz Section (5 Marks) ---")
    try:
        quiz = int(input("Enter the viva/quiz rating (e.g., 2 for full marks):\n"))
    except ValueError:
        print("Invalid numerical input. Viva marks set to 0.")
        quiz = 0

    marks_viva = viva(quiz)
    total_marks += marks_viva

    # --- 4. Calculate Course Completion Marks (10 max) ---
    print("\n--- Course Completion Section (10 Marks) ---")
    try:
        comp = int(input("Enter how much % course completed (e.g., 100):\n"))
    except ValueError:
        print("Invalid numerical input. Completion marks set to 0.")
        comp = 0

    date2 = input("Enter the date of course completed (e.g., 10 november 2025):\n")

    marks_completion = completionornot(comp, date2)
    total_marks += marks_completion

    # --- 5. Output and File Writing ---

    print("\n" + "=" * 40)
    print(f"CALCULATION COMPLETE: {name} (Reg No: {reg_no})")
    print(f"TOTAL INTERNAL MARKS: {total_marks} / 35")
    print("=" * 40)

    file = open("student.txt", "a")
    file.write("----------------------------------------\n")
    file.write(f"Name: {name}\n")
    file.write(f"Registration_number: {reg_no}\n")
    file.write(f"Marks for Certification: {marks_certification}/10\n")
    file.write(f"Marks for Assignment: {marks_assignment}/10\n")
    file.write(f"Marks for Course Completion: {marks_completion}/10\n")
    file.write(f"Marks for Viva: {marks_viva}/5\n")
    file.write(f"FINAL TOTAL MARKS: {total_marks}/35\n")
    file.write("----------------------------------------\n")
    file.close()

    print(f"All data written to student.txt.")