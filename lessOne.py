name = input('Ваше имя ? : ')


print('Куда поедем?')
print('1 - IK')
print('2 - Горы')
print('3 - речка')

question_1 = input('Ваш вариант: ')
question_2 = input('Ваш вариант: ')

if question_1 == '1' :
    print('Привет ' + name  + 'Го на ИК')
    print('Купаться или спать на пляже ')
    question_2 = input('Ваш Вариант: ?')
if question_2 == '2' :
        print('')
elif question_2 == 'спать на пляже' :
            print('')
if question_1 == '2' :
    print('Привет ' + name  + 'Го в горы')
    
