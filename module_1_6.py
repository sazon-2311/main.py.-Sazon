# Работа со словарями
my_dict={'Pavel' : 1998,'Valera' : 2004}
print(my_dict.get('Pavel'))
print(my_dict.get('lev',))
my_dict.update({'Nic': 1980,
                'Ivan': 1990})
del my_dict['Valera']
print(my_dict)
# Работа с множествами
my_set={1,1,3,3,5,5,'top','top',1.34}
print(my_set)
my_set.add(32.55)
my_set.add('spy')
my_set.remove('top')
print(my_set)
