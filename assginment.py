def assign_requirements(number, date):
    """
    Calculates marks (max 10) based on assignment completion requirements.
    Assumes 35 programmes completed by the 20th of November.
    """
    mark = 0
    # Check if the requirements for full marks are met
    if number == 35 and date == 20:
        mark = 10

    # Always return the mark (10 or 0)
    return mark

