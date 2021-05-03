
def fibonacci(n:int) ->int:
    """
    n: the required nth position n the series
    return an ( int ) with nth value in the fibonacci series
    """
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n:int) ->int:
    """
    n: the required nth position n the series
    return an ( int ) with nth value in the lucas numbers series
    """
    if n<=0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


def sum_series(n: int, v1=0, v2=1) ->int :
    """
    n: the required nth position n the series
    v1: value of first number in the series
    v2: value of second number in the series
    return an ( int ) with nth value in the series based on the optional inputs
    by default: assumes the fibonacci series
    """
    if n<=0:
        return v1
    elif n==1:
        return v2
    else:
        return sum_series(n-1,v1,v2)+sum_series(n-2,v1,v2) 

print(sum_series(4,2,1))