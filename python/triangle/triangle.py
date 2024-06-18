def is_triangle(sides) -> bool:
    """Determine if sides supplied define a valid triangle
        
    :param sides: array int - number of sides
    :return: bool - Returns if supplied data defines a valid triangle.
    
     This function checks whether the given side lengths form a valid triangle. It returns True if they do and False         
     otherwise. Triangle as defined by all the following being true: a + b ≥ c | b + c ≥ a | a + c ≥ b | all sides must have        positive nonzero values.
    """

    #define variables
    side_a: float = 0
    side_b: float = 0
    side_c: float = 0
        
    side_a, side_b, side_c = sides
    if side_a <= 0 or side_b <= 0 or side_c <= 0: return False
    if side_a + side_b < side_c or side_b + side_c < side_a or side_a + side_c < side_b: return False
    
    return True


def equilateral(sides) -> bool:
    """
    :param sides: array int - number of sides
    :return: bool - Returns if supplied data defines equilateraltriangle.
    
    This function determines whether the triangle is equilateral. It relies on the is_triangle function to ensure the input is     a valid triangle.
    """
    #define variable(s)
    side_a: float = 0
    side_b: float = 0
    side_c: float = 0
        
    side_a, side_b, side_c, = sides
    if is_triangle(sides) == False: return False      
     
    return side_a == side_b and side_b == side_c


def isosceles(sides) -> bool:
    """This function checks if the triangle is isosceles.
    
    :param sides: array int - number of sides
    :return: bool - Returns if supplied data defines an isosceles triangle.
    
    It uses the is_triangle function to validate the input. Dependent on is_triangle() and if any two sides are equal. Note        that for the purposes of this we do not use the exclusive definition of isoceles (i.e. iff two sides equal)
    """
    #define variable(s)
    side_a: float = 0
    side_b: float = 0
    side_c: float = 0
    
    side_a, side_b, side_c, = sides
    if is_triangle(sides) == False: return False       
    return side_a == side_b or side_a == side_c or side_b == side_c


def scalene(sides: float) -> bool:
    """this function identifies whether the triangle is scalene
    
    :param sides: array int - number of sides
    :return: bool - Returns if supplied data defines a scalene triangle.
    
    Scalene triangle = no sides equal length. It depends on the is_triangle function.
    """
    #define variable(s)
    side_a: float = 0
    side_b: float = 0
    side_c: float = 0
    
    side_a, side_b, side_c, = sides
    if is_triangle(sides) == False: return False
      
    return side_a != side_b and side_a != side_c and side_b != side_c
