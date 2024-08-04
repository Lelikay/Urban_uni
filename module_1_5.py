immutable_var = (1, 'Lelikay', True, 4.0, 'tuble')
print ('immutable_var: ', immutable_var)
# immutable_var [0] = 2
# print(immutable_var)
# не работает, так как кортеж не поддерживает обращение по элементам

immutable_list = [1, 'Lelikay', True, 4.0, 'list']
print ('immutable_list: ', immutable_list)
immutable_list [1] = 'Alex'
print ('Modified immutable_list: ', immutable_list)
