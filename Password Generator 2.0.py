'''
Trying to biuld a good password generatoooorrrrrrr
cause PG 1.0 sucks
Couple of assumptions
Password length is always 9
and only combination of letters number and  basic spc charac
'''
import random

password = ''


def alpha():
    global password
    password = ''
    alphabets = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    alpha = alphabets.split()
    for i in range(0, 8):
        counter = random.randint(0, 8)
        password += alpha[counter]
    return (password)


def numb():
    global password
    password = ''
    for i in range(1, 9):
        dummy = str(random.randint(0, 8))
        password += dummy
    return (password)


def spc():
    global password
    password = ''
    spc = ['!', "@", "#", '$', '%', '^', '&', '*', '(', ')', '-', '+']
    for i in range(0, 8):
        counter = random.randint(0, 8)
        password += spc[counter]
    return (password)


while True:
    print("""
    1.alphabets
    2.numbers
    3.Special Characters
    4.All of the above  
    5.Exit
    """)
    variable = int(input('Enter the desired number (only 1 input)'))
    if variable == 1:
        var1 = alpha()
        print(var1)
    elif variable == 2:
        var2 = numb()
        print(var2)
    elif variable == 3:
        var3 = spc()
        print(var3)
    elif variable == 4:
        password = ''
        var4 = alpha()
        var5 = numb()
        var6 = spc()
        for i in range(3):
            counter = random.randint(0, 7)
            password = var4[counter] + var5[counter] + var6[counter]
            '''   NOICE '''
            print(password,end='')
    else:
        break
