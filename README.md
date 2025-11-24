# vityarthi
Internal Marks Calculator (35 Marks Total)

This is a simple Python project designed to calculate a student's final internal marks out of a total of 35, based on four distinct components: Certifications, Assignments, Course Completion, and Viva/Quiz.

🎯 Project Goal

To accurately sum the marks from four separate modules to determine the student's total internal assessment score (Max 35 Marks).

📊 Mark Distribution

The 35 total marks are broken down into the following components:

Certifications: 10 Max Marks (Criteria: 5 certifications completed)

Assignments: 10 Max Marks (Criteria: 35 assignments completed by Nov 20)

Course Completion: 10 Max Marks (Criteria: 100% completion by '10 november 2025')

Viva/Quiz: 5 Max Marks (Criteria: Viva/Quiz rating of 2)

TOTAL: 35 Marks

📁 File Structure

The project is modularized into five Python files. Each calculation function returns its specific mark, which is then aggregated by the main script.

main_calculator.py:

Description: The main execution script. It handles all user input, calls the functions from the other modules, calculates the grand total, and writes the final results.

Function: Execution block (if __name__ == '__main__':)

certifications_required.py:

Description: Manages the initial student details (Name, Reg No) and calculates marks based on the number of certifications completed (Max 10).

Function: get_certification_marks()

assginment.py:

Description: Calculates marks for the assignment component (Max 10).

Function: assign_requirements(number, date)

vityarthi.py:

Description: Calculates marks for the course completion component (Max 10).

Function: completionornot(comp, date)

viva.py:

Description: Calculates marks for the viva/quiz component (Max 5).

Function: viva(num1)

🚀 How to Run the Project

Ensure all five Python files (main_calculator.py, certifications_required.py, assginment.py, vityarthi.py, viva.py) are in the same directory.

Open your terminal or command prompt.

Navigate to the project directory.

Run the main script using the Python interpreter:

python main_calculator.py


The script will prompt you for input sequentially for each section.

💾 Output

Upon successful completion, the script will:

Display the final calculated marks in the console.

Append a detailed breakdown of all marks, along with the student's information, to a file named student.txt.
