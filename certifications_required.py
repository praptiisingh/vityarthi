def get_certification_marks():
    """
    Handles student input for certifications and calculates marks (max 10).
    Returns a tuple: (name, reg_no, marks_certification)
    """
    print("welcome student")
    marks_certification = 0

    # Global variables for name and registration number (used by the main script)
    global name, reg_no
    name = input("enter your name\n")
    reg_no = input("enter your registration no\n")

    try:
        a = int(input("enter the number of (hackerrank+sololearn+greatlearning) certification completed (max 5)\n"))
    except ValueError:
        print("Invalid input for certifications. Assuming 0.")
        a = 0

    if a == 5:
        marks_certification = 10
    elif a == 4:
        marks_certification = 8
    elif a == 3:
        marks_certification = 6
    else:
        print("You failed to meet completion criteria for full certification marks.")

    return (name, reg_no, marks_certification)