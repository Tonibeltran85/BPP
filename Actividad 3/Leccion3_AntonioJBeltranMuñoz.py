def string_reverse(str1):
    '''
    Returns the reversed String.

    Parameters:
        str1 (str):The string which is to be reversed.

    Returns:
        reverse(str1):The string which gets reversed.   
    '''

    reverse_str1 = ''
    i = len(str1)
    while i > 0:
        reverse_str1 += str1[i - 1]
        i = i- 1
    return reverse_str1

class CalculadoraClass:
    '''Calculator Class.'''

    def __init__(self, a , b):
        '''
        Constructor Class constructor where the value of the parameters is set.
        Parameters:
        ---------
        a : int
            first value to multiply.
        b: int
            second value to multiply.
        '''
        self.a = a
        self.b = b

def multiplier(a, b):
    """Takes in two numbers, returns their product.
    Parameters
        ---------
        a: int
            first value to multiply.
        b: int
            second value to multiply.
    Returns:
        -------
        a*b : int
            result of the multiplication   
    """   
    return a*b

