import math
#zad1
# a = input('Podaj liczbę: ')
# b = input('Podaj liczbę: ')
# try:
#     a = int(a)
#     b = int(b)
#     c = a ** 2 + a * b + b ** 2
#     with open('zadanie1.txt', 'w') as file:
#         file.write(f'Wynik wynosi {str(c)}')
#
# except ValueError:
#     print('Podałeś złe dane')

#zad2
# def suma_list(lista1, lista2):
#     lista3 = []
#     for x, y in zip(lista1, lista2):
#         lista3.append(x + y)
#     return lista3
# lista1 = [2, 5, 6, 8, 12]
# lista2 = [44, 8, 9, 15, 2]
# print(suma_list(lista1, lista2))

#zad3
# with open('tekst.txt', 'r', encoding='utf8') as file:
#     zawartosc = file.read()
#     znaki = zawartosc[100:135]
# duze_litery = [x for x in znaki if x.isupper()]
# if len(duze_litery) == 0:
#     print('Tekst zawiera 0 dużych liter')
# else:
#     print(duze_litery)
#     print('Tekst zawiera ' + str(len(duze_litery)) + ' dużych liter')

#zad4
# lista_z_liczbami = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = int(input('Podaj liczbę: '))
# lista_z_liczbami2 = [x for x in lista_z_liczbami if x > a]
#
# print(lista_z_liczbami)
# print(lista_z_liczbami2)

#zad5
# a = (math.exp(3) + math.cos(39)**2)**(1/5) + (2/7)**3 + math.pi
# print(f'wynik wynosi {a:.2f}')