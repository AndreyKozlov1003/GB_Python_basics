#задание 1
s = [1, 'Andrey', 2.896, [1,2,3]]
for i in range (0,len(s)):
    print (type(s[i]))


#задание 2
s = []
exit = False
while exit == False:
    elem = input ('Введите элемент в список. ' 
                  'Если хотите выйти,напишите "выход": ')
    if elem == 'выход':
        exit = True
    else:
        s.append(elem)
print ('Начальный список - {}'.format(s))

change = [0,0]
for i in range(0,len(s)-1,2):
    change[0] = s[i]
    change[1] = s[i+1]
    s[i] = change[1]
    s[i+1] = change[0]
print('Перемешанный список - {}'.format(s))

#задание 3
#вариант через dict
mes = {'зима' : [12,1,2],
       'весна' : [3,4,5],
       'лето' : [6,7,8],
       'осень' : [9,10,11]   
}
num = list(mes.values())
state = list(mes.keys())
state = list(enumerate(state))
number = int(input('Введите номер месяца, а я скажу, какой это сезон года - '))
for i in range (0,len(num)):
    if num[i].count(number) != 0:
        print('Сейчас - {}'.format(state[i][1]))
        
#вариант через list
state = ['зима', 'весна', 'лето', 'осень']
num = int(input('Введите номер месяца - '))
if num == 12 or num == 1 or num == 2:
    print('Сейчас на дворе - {}'.format(state[0]))
elif num == 3 or num == 4 or num == 5:
    print('Сейчас на дворе - {}'.format(state[1]))
elif num == 6 or num == 7 or num == 8:
    print('Сейчас на дворе - {}'.format(state[0]))
elif num == 9 or num == 10 or num == 11:
    print('Сейчас на дворе - {}'.format(state[0]))

        
#задание 4 
input_str = input ('Введите несколько слов, разделенные пробелами - ')
words = input_str.split()
for i in range(0,len(words)):
    if len(words[i]) > 10:
        print('{}. {}'.format(i+1,words[i][0:10]))
    else:
        print('{}. {}'.format(i+1,words[i]))


#задание 5
rate = [7, 5, 3, 3, 2]
elem = int(input('Введите новый элемент рейтинга, ' 
                 'который является натуральным числом - '))
length_start = len(rate)
for i in range (0,len(rate)):
    if rate[i] < elem:
        rate.insert(i,elem)
        break
    elif rate[i] == elem:
        if rate.count(elem) != 1:
            rate.insert(i+rate.count(elem),elem)
            break
        else:
            rate.insert(i+1,elem)
            break
    elif rate[i] > elem:
        pass
if length_start == len(rate):
    rate.insert(len(rate),elem)
print('Обновленный рейтинг: {}'.format(rate))


#задание 6
#формирование структуры Товары по введенным данным пользователя
exit = ''
base = []
i = 1
while exit != 'выход':
    base.append ((i,{'название': input('Введите название товара - '), 
                  'цена': float(input('Введите цену товара в рублях - ')),
                  'количество': int(input('Введите количество - ')),
                  'ед': input('В каких единицах товар - ')
                 }))
    i += 1
    exit = input('Для продолжения ввода товаров в базу нажмите Enter. '
                 'Для выхода введите "выход" - ')
print ('{}Структура "Товары" по вашему запросу сформирована: '.format('\n'))
print(base)

#формирование аналитики по Товарам
product_analytics = {
    'название' : [],
    'цена' : [],
    'количество' : [],
    'ед' : []
}
for i in range (0, len(base)):
    product_analytics.get('название').append(base[i][1].get ('название'))
    product_analytics.get('цена').append(base[i][1].get ('цена'))
    product_analytics.get('количество').append(base[i][1].get ('количество'))
    product_analytics.get('ед').append(base[i][1].get ('ед'))
    
print('{}Товарная аналитика произведена: '.format('\n'))
print(product_analytics)




