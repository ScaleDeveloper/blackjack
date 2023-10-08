koldra = [6,7,8,9,10,2,3,4,11] * 4

import random
random.shuffle(koldra)

print('Поиграем в очко?')
count = 0

while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        current = koldra.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count >15:
            print('Извини,ты проиграл.')
            break
        elif count == 15:
            print('Поздравляю,вы выиграли!')
            break
        else:
            print('у вас %d очков.' %count)
    elif choise == 'n':
        print('у вас %d очков и ваша игра закончена, конечная.' %count)
        break


print('До новых встреч, удачи!')

