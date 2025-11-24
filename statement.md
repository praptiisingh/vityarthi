Project Statement: Internal Marks Calculator

1. Problem Statement

In academic settings, internal assessment marks (often referred to as sessional or continuous evaluation marks) are calculated by aggregating scores from multiple disparate components such as certifications, assignments, and viva. Manually tracking and calculating these scores across various criteria is time-consuming, prone to human error, and lacks transparency.

The problem this project addresses is the need for an efficient, modular, and reliable automated system to aggregate a student's marks from all internal assessment components into a single, accurate final score out of 35.

2. Scope of the Project

The scope of this project is limited to:

Input Collection: Gathering required data points from the user (student name, registration number, component scores/completion status).

Modular Calculation: Utilizing separate Python modules to calculate marks for four distinct components (Certification, Assignment, Course Completion, Viva).

Total Aggregation: Calculating the grand total internal mark (Max 35).

Reporting: Generating a detailed output to the console and persisting the student's record and mark breakdown into a student.txt file.

The project does not include a graphical user interface (GUI), database integration (beyond the flat file), or advanced authentication mechanisms.

3. Target Users

The primary target users for this system are:

Academic Coordinators/Faculty: To quickly and accurately calculate and record internal assessment scores for a class of students.

Students: To understand the exact breakdown of their internal marks based on the specific criteria.

4. High-Level Features

Calculate marks for Certifications (out of 10).

Calculate marks for Assignments (out of 10).

Calculate marks for Course Completion (out of 10).

Calculate marks for Viva/Quiz (out of 5).

Aggregate all component marks to a final score (out of 35).

Store student records and mark breakdown in a flat file (student.txt)
