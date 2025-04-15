def ieee(number):
    # check the sign
    sign = '0' if number >= 0 else '1'

    # divide the number into integer and decimal parts 
    integer = int(number)
    decimal = number - integer