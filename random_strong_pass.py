import random
a1 = 'abcdefghijklmnopqrstuvwxyz'
a2 = 'abcdefghijklmnopqrstuvwxyz'
a3 = 'abcdefghijklmnopqrstuvwxyz'
A1 = 'ABCDEFGHIJKLMNOPQRstUVWXYZ'
A2 = 'ABCDEFGHIJKLMNOPQRstUVWXYZ'
A3 = 'ABCDEFGHIJKLMNOPQRstUVWXYZ'
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
sp = ['~!@#', '#@$%', '/.*&','%!*#$', '*@^#', '&!#^', '^!%$', '!*^#', '-!~^', '_!%~', '@_-!', '~_$`', '#~*^', '+(~*', '~#(_', '~)$_']
ss = ['~','`','@','#','$', '%', '^', '&', ' ', '*', '(', ')', '-', '_', '+', '=']

password = f"{a1[random.randint(0, 25)]}{random.choice(ss)}{A1[random.randint(0, 25)]}{num1}{a2[random.randint(0, 25)]}{random.choice(sp)}{A2[random.randint(0, 25)]}{num2}{a3[random.randint(0, 25)]}{A3[random.randint(0, 25)]}{num3}{random.choice(ss)}"
print(password)
