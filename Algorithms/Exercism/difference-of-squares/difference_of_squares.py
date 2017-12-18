def square_of_sum(n):
    return pow( (n * (n+1)) /2 ,2)

def sum_of_squares(n):
    sum_value = 0
    for i in xrange(n+1):
        sum_value += (i*i)
    return sum_value

def difference(n):
    print square_of_sum(2)
    print sum_of_squares(n)
    return square_of_sum(n) - sum_of_squares(n)

