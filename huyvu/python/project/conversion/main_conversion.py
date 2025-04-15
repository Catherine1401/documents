from convert_library import convert as cv
from convert_library import test

# treat input data
mark = 0
try:
    input_number_system = int(input('enter input number system: '))
    output_number_system = int(input('enter output number system: '))
except:
    input_number_system = output_number_system = 2
    mark = 1
if test.test_number_system(input_number_system) == False or test.test_number_system(output_number_system) == False:
    input_number_system = output_number_system = 2
    mark = 1
if input_number_system == 2:
    try:
        input_number = float(input('enter number to convert: '))
    except:
        input_number = 0
        mark = 1
    if test.test_number_for_2(input_number) == False:
        input_number = 0
        mark = 1
elif input_number_system == 8:
    try:
        input_number = float(input('enter number to convert: '))
    except:
        input_number = 0
        mark = 1
    if test.test_number_for_8(input_number) == False:
        input_number = 0
        mark = 1
elif input_number_system == 10:
    try:
        input_number = float(input('enter number to convert: '))
    except:
        input_number = 0
        mark = 1
    if test.test_number_for_10(input_number) == False:
        input_number = 0
        mark = 1
else:
    try:
        input_number = str(input('enter number to convert: '))
    except:
        input_number = '0'
        mark = 1
    if test.test_number_for_16(input_number) == False:
        input_number = '0'
        mark = 1

# convert to decicmal number system
if input_number_system != 10:
    if input_number_system == 2:
        input_number = cv.binary_decimal(input_number)
    elif input_number_system == 8:
        input_number = cv.octal_decimal(input_number)
    else:
        input_number = cv.hexadecimal_decimal(input_number)

# convert according to user preferences
if output_number_system == 2:
    output_number = cv.decimal_binary(input_number)
elif output_number_system == 8:
    output_number = cv.decimal_octal(input_number)
elif output_number_system == 10:
    output_number = input_number
else:
    output_number = cv.decimal_hexadecimal(input_number)

# export data
if mark == 1:
    print('input error, please enter again')
else:
    print(output_number)