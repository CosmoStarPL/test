import sys
from colorama import init, AnsiToWin32
init ( wrap = False)
stream = AnsiToWin32(sys.stderr).stream


print(Fore.BLUE)
#int
number =  13
#float
fnumber = 5.7
#str
name = "Shoxrux"
#bool
status = True

# вывод коментарии
# можеш писать что угодно
print( "Что нужно вывести")
print( name )
# экранирования
print( "он \"плохой\" человек" )
# преревод строки
print( 'привет \n мир' )
#конктенация
print( "привет меня зовут " + name )
print( "мне " + str ( number ) +  " лет" )
ilo = input("Ведите имя: ")
loi = input("Веди возраст: ")

print("Привет " + ilo )
print("Ты стар " + loi )
# +, -,*, /, **, %
a = 5
b = 10
c = a+b
print (c)
f = 11

f =-f
f =-f
print(f)
#калькулятор
what = input( "Что делаем? (+,-):" )

q = float(input( "первое число:  " ))
w = float(input( "второе чило:  " ))

if what == "+":
    e = q + w
    print("Резулбтат " + str(e))
elif what == "-":
    e = q - w
    print("результат " + str(e))
else:
    print("ты дебил там написано выберайте плюс или минус")
