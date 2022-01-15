from sys import argv

script_name, hours, rate, bonus = argv
print('Задание 1 по запуску скрипта с параметрами')
salary = int(hours)*int(rate) + int(bonus)
print('Расчетная заработная плата составила {} рублей'.format(salary))
