a = input('Введите первое число =')
b = input('Введите второе число =')
c = input('Введите третье число =')
if a == b and b == c and a == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)