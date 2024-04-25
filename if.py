x = 50
print('Привет')
if x < 0:
    print('Неа')
if x >= 40:
    print('Годнота')
print('Пока')

a, i, b = 20, 100, 5
if a < i:
    print('ok')
if (a + b) < (i - a):
    print('ok')
if (a > b) and (i > a):
    print('okei)))')
if 20 == a or i == 20:
    print('nea')
if (a < i) and (b > 0 or 100 == i):
    print('okeyna')

if '985' > '2024':
    print('ok')
if [5, 20, 100] < [5, 50, 500]:
    print('okeyna')

# ошибка if '1985' < 2024
#    print('ok')
if '65' != 55:
    print('???')