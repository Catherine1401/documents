# storing data
mark3 = 0
try:
    integrer = int(input('nhap so nguyen: '))
except:
    integrer = 0
    mark3 = 1
binary = list(bin(integrer))
storage = ''
if binary[0] == '-':
    del binary[0:3]
    mark = 1
else: 
    del binary[0:2]
    mark = 0
binary.reverse()
for i in range(len(binary), 8):
    binary.append('0')

if mark == 0:
    for i in range(0, len(binary)):
        storage = binary[i] + storage
else:
    for i in range(0, len(binary)):
        if binary[i] == '0':
            storage = binary[i] + storage
        else:
            storage = '1' + storage
            mark1 = i + 1
            break
    for i in range(mark1, len(binary)):
        if binary[i] == '0':
            storage = '1' + storage
        else:
            storage = '0' + storage

# exporting data
storage1 = list(storage)
integrer = 0
storagee = storage1[::-1]
mark2 = 1
if mark == 1:
    mark2 = -1
    for i in range(0, len(storagee)):
        if storagee[i] == '1':
            mark4 = i + 1
            break
    for i in range(mark4, len(storagee)):
        if storagee[i] == '0':
            storagee[i] = '1'
        else:
            storagee[i] = '0'
for i in range(0, len(storagee)):
    integrer += int(storagee[i]) * 2 ** i

# print result
if mark3 == 0:
    print(storage)
    print(integrer * mark2)
else:
    print('input erorr, please typing again')