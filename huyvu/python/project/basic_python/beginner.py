
# print("xin chao","ket thuc","cham het",sep=", ",end="!!\n")

# a = 10.1232567865437
# print("%.4f" %a)

# try:
#     a = int(input("hay nhap vao mot so nguyen: "))
# except:
#     a = "loi so lieu, vui long nhap lai"
# print(a)


# try:
#     a = int(input("nhap mot so nguyen: "))
#     if a%2 == 0:
#         print("a la so chan")
#     else:
#         print("a la so le")
# except:
#     a = 0
#     print("loi nhap lieu, vui long nhap lai",)
    
# try:
#     a = float(input("nhap mot so: "))
#     if a > 0:
#         print("so duong")
#     elif a == 0:
#         print("so 0")
#     else:
#         print("so am")
# except:
#     a = 0
#     print("loi nhap lieu, vui long nhap lai")

# a = [1,2,3,4,5,6,7,8,9]
# for i in range(0,len(a)):
#     print(i, a[i])

# a = [1,2,3,4,5]
# sum = 0
# for i in range(0,len(a)):
#     sum += a[i]
# print(sum)

# a = [1,2,3,4,5]
# sum = 0
# for i in range(0,len(a)):
#     if a[i]%2 == 0:
#         sum += 1
# print(sum)

# a = [1,2,3,4,5]
# max = a[0]
# for i in range(0,len(a)):
#     if max < a[i]:
#         max = a[i]
# print(max)

# a = []
# try:
#     n = int(input("nhap so phan tu cua mang: "))
# except:
#     n = 0
# for i in range(0,n):
#     try:
#         temp = float(input("nhap phan tu thu " + str(i+1) + ": "))
#         a.append(temp)
#     except:
#         temp = str("loi")
#         break
# if n == 0 or temp == "loi":
#     print("loi nhap lieu, vui long nhap lai")
# else:
#     print(a)

# a = []
# try:
#     row = int(input("nhap so hang: "))
# except:
#     row = 0
# for i in range(0,row):
#     try:
#         temp = int(input("nhap so phan tu cua hang " + str(i+1) + ": "))
#     except:
#         temp = 0
#         break
#     a_row = []
#     for j in range(0,temp):
#         try:
#             temp1 = int(input("nhap du lieu cho hang " + str(i+1) + " cot " + str(j+1) + ": "))
#         except:
#             temp1 = 0
#             break
#         a_row.append(temp)
#     if temp1 == 0:
#         break
#     else:
#         a.append(a_row)

# if row == 0 or temp == 0 or temp1 == 0:
#     print("loi nhap lieu, vui long nhap lai")
# else:
#     sum = le = chan = 0
#     max = min = a[0][0]
#     for i in range(0,len(a)):
#         for j in range(0,len(a[i])):
#             sum += a[i][j]
#             if a[i][j]%2 == 0:
#                 chan += 1
#             else:
#                 le += 1
#             if max < a[i][j]:
#                 max = a[i][j]
#             if min > a[i][j]:
#                 min = a[i][j]
#     print(sum,le,chan,max,min,sep="\n")
 
# file = open("a.txt","w")
# file.write("day la dong 1\n")
# file.write("day la dong 2")

# file1 = open("a.txt","r")
# file2 = open("b.txt","w")
# a = []
# for i in file1:
#     for j in i.split():
#         file2.write(j + "\n")
# file1.close()
# file2.close()

# def hello(language):
#     print("hello " + language)
# hello("c++")

# def printmax(a,b):
#     if a < b:
#         a = b
#         print(a)
# a = float(input("nhap so thu 1: "))
# b = float(input("nhap so thu 2: "))
# printmax(a,b)

# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-1) + f(n-2)
# a = int(input("Nhap so can tinh: "))
# print(f(a))
    
# def luythua(a,b):
#     i = 1
#     if a == 0 and b == 0: return "loi"
#     elif b==0: return 1
#     else:
#         if b>0:
#             while(i<b):
#                 a*=a
#                 i+=1
#             return a
#         else:
#             while(i<b*-1):
#                 a*=a
#                 i+=1
#             a=1/a
#             return a
# a = int(input("nhap so can tinh: "))
# b = int(input("nhap so mu: "))
# print(luythua(a,b))

# a = """
# hello
# my name is Huy
# iam dep trai nhat the gioi
# me yeu @lthuhuongg rat rat x1000 nhieu"""
# print(a.replace('yeu','ghet'))

# def giaithua(n):
#     if n == 0: return 1
#     return n*giaithua(n-1)
# print(giaithua(123))

#a = dict({"A":2,"B":3,"C":4})
#b = {"a":1,"b":2,"c":{"d":1}}
#for i in b:
#   print(i)
#print(b.values())

# a = input('nhap chuoi thu nhat: ')
# b = input('nhap chuoi thu hai: ')
# print(a+ ' '+b)

# a = (1,2,3,4,5,6,7,8,9)
# b = []
# for i in range(0,len(a)):
#     if a[i]%2 == 0:
#         b.append(a[i])
# a = tuple(b)
# print(a)

# a = {1,2,3,4,5,6,7,8,9}
# b = {2,4,6,8,10,12}
# b = a.difference(b)
# print(a.difference(b))

# try:
#     n = int(input('hay nhap so n: '))
# except:
#     n = 0
# if n<=0: print('loi nhap lieu, vui long nhap lai')
# else:
#     temp = dict()
#     for i in range(1,n+1):
#         temp[i] = i*i
#     print(temp)