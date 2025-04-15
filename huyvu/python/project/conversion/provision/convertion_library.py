class convert:
    def binary_decimal(binary_number):
        # xu ly dau vao
        if binary_number < 0:
            binary_number *= -1
            mark = -1
        else:
            mark = 1
        binary_number = str(binary_number)
        decimal = 0

        # tim dau phay
        point_position = binary_number.find('.')
        if point_position == -1:
            point_position = len(binary_number)

        # xu ly phan nguyen
        for i in range(point_position):
            decimal  += int(binary_number[i]) * 2 ** (point_position - i - 1)

        # xu ly phan thap phan
        for i in range(point_position + 1,len(binary_number)):
            decimal += int(binary_number[i]) * 2 ** (point_position - i)

        return decimal * mark
    def octal_decimal(octal_number):
        # xu ly dau vao
        mark = 1
        if octal_number < 0:
            octal_number *= -1
            mark = -1
        octal_number = str(octal_number)
        decimal = 0

        # tim dau phay
        point_position = octal_number.find('.')
        if point_position == -1:
            point_position = len(octal_number)

        # xu ly phan nguyen
        for i in range(point_position):
            decimal += int(octal_number[i]) * 8 ** (point_position - i - 1)

        # xu ly phan thap phan
        for i in range(point_position + 1,len(octal_number)):
            decimal += int(octal_number[i]) * 8 ** (point_position - i)

        return decimal * mark
    def hexadecimal_decimal(hexadecimal_number):
        # xu ly dau vao
        hexadecimal = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        mark = 1
        if str(hexadecimal_number)[0] == '-':
            hexadecimal_number = str(hexadecimal_number).replace('-','')
            mark = -1
        hexadecimal_number = str(hexadecimal_number)
        decimal = 0

        # tim dau phay 
        point_position = hexadecimal_number.find('.')
        if point_position == -1:
            point_position = len(hexadecimal_number)

        # xu ly phan nguyen
        for i in range(point_position):
            decimal += hexadecimal[hexadecimal_number[i]] * 16 ** (point_position - i - 1)

        # xu ly phan thap phan
        for i in range(point_position + 1, len(hexadecimal_number)):
            decimal += hexadecimal[hexadecimal_number[i]] * 16 ** (point_position - i)

        return decimal * mark
    def decimal_binary(decimal_number):
        # xu ly dau vao
        mark = ''
        if decimal_number < 0:
            decimal_number *= -1
            mark = '-'
        # xu ly phan nguyen
        intergral_decimal = int(decimal_number)
        intergral_binary = ''
        while intergral_decimal != 0:
            intergral_binary = str(intergral_decimal % 2) + intergral_binary
            intergral_decimal //= 2

        # xu ly phan thap phan 
        fractional_decimal = decimal_number - int(decimal_number)
        fractional_binary = ''
        print(fractional_decimal)
        i = 0
        while fractional_decimal != 0 and i < 17:
            last_intergral = int(fractional_decimal * 2)
            fractional_binary += str(last_intergral)
            fractional_decimal = fractional_decimal*2 - last_intergral
            print(fractional_decimal)
            i += 1
        # xu ly dau ra
        if fractional_binary:
            binary = intergral_binary + '.' + fractional_binary
        else:
            binary = intergral_binary
        return mark + binary
    def decimal_octal(decimal_number):
        # xu ly dau vao
        mark = ''
        if decimal_number < 0:
            decimal_number *= -1
            mark = '-'

        # xu ly phan nguyen
        intergral_decimal = int(decimal_number)
        intergral_octal = ''
        while intergral_decimal != 0:
            intergral_octal = str(intergral_decimal % 8) + intergral_octal
            intergral_decimal //= 8

        # xu ly phan thap phan
        fractional_decimal = decimal_number - int(decimal_number)
        fractional_octal = ''
        i = 0
        while fractional_decimal != 0 and i < 17:
            last_intergral = int(fractional_decimal * 8)
            fractional_octal += str(last_intergral)
            fractional_decimal = fractional_decimal * 8 - last_intergral
            i += 1

        # xu ly dau ra
        if fractional_octal:
            octal = intergral_octal + '.' + fractional_octal
        else:
            octal = intergral_octal
        return mark + octal
    def decimal_hexadecimal(decimal_number):
        # xu ly dau vao
        hexadecimal = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        mark = ''
        if decimal_number < 0:
            decimal_number *= -1
            mark = '-'

        # xu ly phan nguyen
        intergral_decimal = int(decimal_number)
        intergral_hexadecimal = ''
        while intergral_decimal != 0:
            intergral_hexadecimal = str(hexadecimal[intergral_decimal % 16]) + intergral_hexadecimal
            intergral_decimal //= 16

        # xu ly phan thap phan
        fractional_decimal = decimal_number - int(decimal_number)
        fractional_hexadecimal = ''
        i = 0
        while fractional_decimal != 0 and i < 17:
            last_intergral = int(fractional_decimal * 16)
            fractional_hexadecimal += str(hexadecimal[last_intergral])
            fractional_decimal = fractional_decimal * 16 - last_intergral
            i += 1

        # xu ly dau ra
        if fractional_hexadecimal:
            hexa = intergral_hexadecimal + '.' + fractional_hexadecimal
        else:
            hexa = intergral_hexadecimal
        return mark + hexa

class test:
    def test_number_system(input_number_system):
        test = [2,8,10,16]
        if input_number_system in test:
            result = True
        else:
            result = False
        return result
    def test_number_for_2(input_number):
        test = ['-','.','0','1']
        result = True
        for i in range(len(str(input_number))):
            if str(input_number)[i] not in test:
                result = False
        return result 
    def test_number_for_8(input_number):
        test = ['-','.','0','1','2','3','4','5','6','7']
        result = True
        for i in range(len(str(input_number))):
            if str(input_number)[i] not in test:
                result = False
        return result
    def test_number_for_10(input_number):
        test = ['-','.','0','1','2','3','4','5','6','7','8','9']
        result = True
        for i in range(len(str(input_number))):
            if str(input_number)[i] not in test:
                result = False
        return result
    def test_number_for_16(input_number):
        test = ['-','.','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        result = True
        for i in range(len(str(input_number))):
            if str(input_number)[i] not in test:
                result = False
        return result
