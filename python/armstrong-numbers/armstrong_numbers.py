def is_armstrong_number(number:int) -> bool:

    """ Determines if a number is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits
    each raised to the power of the number of digits in the number.

    param: number integer: The number to be tested for "Armstrongness"
    return: bool: Is the number supplied an Armstrong number?
    """
    #Define Variables
    number_string = str(number)
    total_sum = 0
    
    for digit in number_string:
        total_sum += int(digit) ** len(number_string)
    
    return total_sum == number