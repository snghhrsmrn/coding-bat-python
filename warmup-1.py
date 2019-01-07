def sleep_in(weekday, vacation):
    """
    The parameter weekday is True if it is a weekday, and the parameter vacation 
    is True if we are on vacation. We sleep in if it is not a weekday or we're on 
    vacation. Return True if we sleep in.
    """
    if not weekday or vacation:
        return True
    else:
        return False
    
def monkey_trouble(a_smile, b_smile):
    """
    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate 
    if each is smiling. We are in trouble if they are both smiling or if neither 
    of them is smiling. Return True if we are in trouble. 
    """
    return a_smile == b_smile

def sum_double(a, b):
    """
    Given two int values, return their sum. Unless the two values are the same,
    then return double their sum.
    """
    return a+b if a!=b else 2*(a+b)

def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, except return 
    double the absolute difference if n is over 21.
    """
    return 2*(n-21) if n>21 else 21-n

def parrot_trouble(talking, hour):
    """
    We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
    We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
    Return True if we are in trouble.
    """
    return talking and hour not in range(7,21)
