#задание 1
'''s = [1, 'Andrey', 2.896, [1,2,3]]
for i in range (0,len(s)):
    print (type(s[i]))'''

#задание 2
'''s = []
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
print('Перемешанный список - {}'.format(s))'''

#задание 3
'''mes = {'зима' : [12,1,2],
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
        print('Сейчас - {}'.format(state[i][1]))'''
        
#задание 4 
input_str = input ('Введите несколько слов, разделенные пробелами - ')
words = input_str.split()
for i in range(0,len(words)):
    if len(words[i]) > 10:
        print('{}. {}'.format(i+1,words[i][0:10]))
    else:
        print('{}. {}'.format(i+1,words[i]))





