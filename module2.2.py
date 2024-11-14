first=int(input('Ведите число:'))
second=int(input('Ведите число:'))
third=int(input('Ведите число:'))
if first == second ==third:
    print('Одинаковых:',3)
elif first == second or first == third or second == third:
    print('Одинаковых:',2)
else:print('Одинаковых:',0)

