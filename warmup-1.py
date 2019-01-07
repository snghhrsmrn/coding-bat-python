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

def makes10(a,b):
    """
    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
    """
    return a==10 or b==10 or a+b==10

def near_hundred(n):
    """
    Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
    """
    return abs(n-100)<=10 or abs(n-200)<=10

def pos_neg(a,b,negative):
    """
    Given 2 int values, return True if one is negative and one is positive. 
    Except if the parameter "negative" is True, then return True only if 
    both are negative.
    """
    if negative:
        return (a<0 and b<0)
    else:
        return (a<0 and b<0) or (a>0 and b<0)
    
def not_string(str):
    """
    Given a string, return a new string where "not " has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    """
    if len(str)>=3 and str[:3]=='not':
        return str
    else:
        return "not" + str
