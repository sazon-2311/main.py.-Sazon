immutable_var=(1,2,'q','spy')
print('immutable_var:',immutable_var)
print(immutable_var[3]) #можно доставать любой элемент
#immutable_var[3]='lit' #нельзя изменять неизменяймый кортеж,
                       #для хранения в нем данных, особеность,
                       #занимает меньше места
print('меньше весит:',immutable_var.__sizeof__())
Module_list=[1,2,'q','spy']
Module_list[3]='Urban'
print(Module_list)
print('больше весит',Module_list.__sizeof__())