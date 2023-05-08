# import math
# # --------------1---------------------
# wynik = (math.exp(4) - math.log(34, 2)) ** (1 / 3)
# print(f'{wynik:.2f}')
#
# # ---------------2------------------
# list1 = [3, 6, 9, 1, 3, 2, 4, 6, 7, 2, 8, 3]
# list2 = [list1[x] for x in range(2, len(list1), 3)]
# print(list1)
# print(list2)
#
# # --------------3----------------------
# def suma_elementow(lista):
#     wynik = lista[0] + lista[-1]
#     zlicz = sum(1 for x in lista if x > wynik)
#     return wynik, zlicz
# moja_lista = [1, 2, 3, 4, 5, 6, 7, 8, 2]
# print(suma_elementow(moja_lista))
# # --------------4----------------------
# with open('tekst (1).txt', 'r', encoding='utf8') as file:
#     file.seek(0)
#     zawartosc = file.read()
#     znaki = zawartosc[48:73]
# print(znaki)
# duze_litery = [x for x in znaki if x.isupper()]
# if len(duze_litery) == 0:
#     print('Tekst zawiera 0 dużych liter')
# else:
#     print(duze_litery)
#     print('Tekst zawiera ' + str(len(duze_litery)) + ' dużych liter')
#
# # -------------------5--------------------
# try:
#     a = int(input('Podaj a:'))
#     b = int(input('Podaj b:'))
#     c = int(input('Podaj c:'))
# except ValueError:
#     print('Złe dane')
#
# if a > 0 and b > 0 and c > 0:
#     if (a ** 2 + b ** 2 == c ** 2):
#         print("Trójkąt jest prostokątny")
#         pole = (a * b) / 2
#         print(f'Pole wynosi {pole}')
#         with open('zadanie5.txt', 'w') as f:
#             f.write(str(pole))
#     else:
#         print("Trójkąt nie jest prostokątny")
# else:
#     print('Podane wartości muszą być liczbami całkowitymi większymi od 0')
