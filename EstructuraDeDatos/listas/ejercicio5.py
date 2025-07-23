# Las listas se pueden indexar y actualizar, 

my_list = [1, None, True, 'Soy una cadena', 256, 0]
print(my_list[3])  # output: Soy una cadena
print(my_list[-1])  # output: 0

my_list[1] = '?'
print(my_list)  # output: [1, '?', True, 'Soy una cadena', 256, 0]

my_list.insert(0, "primero")
my_list.append("último")
print(my_list)  # output: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']

