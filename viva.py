def viva(num1):
    """
    Calculates marks (max 5) based on the viva/quiz result.
    Assumes a score of '2' gives full marks.
    """
    mark = 0
    # Check if the requirement for full marks is met
    if num1 == 2:
        mark = 5

    # Always return the mark (5 or 0)
    return mark

