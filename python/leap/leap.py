def leap_year(year:int) -> bool:
    """Determine if entered year is a leap year.
 
    :param year: int - The year to be tested for leapyearness.
    :return: bool - is_leap_year derived from 'LEAP_YEAR_DIVISOR', 'LEAP_CENTURY_DIVISOR', and 'YEARS_IN_CENTURY'.
 
    Function that determines if a givin year is a leap year based on 'LEAP_YEAR_DIVISOR', 'LEAP_CENTURY_DIVISOR', and 'YEARS_IN_CENTURY'..
    """

    
    #initialize variables
    is_leap_year: bool = False
    LEAP_CENTURY_DIVISOR: int = 400
    LEAP_YEAR_DIVISOR: int = 4
    YEARS_IN_CENTURY: int = 100

    if year % LEAP_YEAR_DIVISOR == 0:
        is_leap_year = True
    if year % YEARS_IN_CENTURY == 0 and year % LEAP_CENTURY_DIVISOR == 0: 
        is_leap_year = True
    if year % YEARS_IN_CENTURY == 0 and year % LEAP_CENTURY_DIVISOR != 0: 
        is_leap_year = False
    
    return is_leap_year
