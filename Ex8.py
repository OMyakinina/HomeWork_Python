'''Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no'''

n = int(input('Ввести длину шоколадки '))
m = int(input('Ввести ширину шоколадки '))
k = int(input('Ввести количество долек '))

if k % m == 0 or k % n == 0:
    print('Можно')
else:
    print('Нельзя')
