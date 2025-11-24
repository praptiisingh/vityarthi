def completionornot(comp, date):
    """
    Calculates marks (max 10) based on course completion percentage and date.
    Assumes 100% completion by '10 november 2025'.
    """
    mark = 0
    # Check if the requirements for full marks are met
    if comp == 100 and date == '10 november 2025':
        mark = 10

    # Always return the mark (10 or 0)
    return mark