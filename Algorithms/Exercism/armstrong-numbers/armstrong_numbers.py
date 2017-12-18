def is_armstrong(number):
    power_value = len(str(number))
    answer = 0
    orginial_number = number

    for i in xrange(power_value):
        answer += pow((number%10),power_value)
        number /= 10

    return answer == orginial_number
