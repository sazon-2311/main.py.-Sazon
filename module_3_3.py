def print_params (a = 1, b = "Строка" , c = True):
    print(a, b, c)


print_params()
print_params(3, 'wb', False)
print_params(b= 25)
print_params(c= [1,2,3])

values_list = [12, "слово", True]
values_dict = {"a" : 25, "b" : "Строка" , "c" : True }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)