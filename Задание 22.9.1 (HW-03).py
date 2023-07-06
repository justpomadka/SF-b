sequence = input('Введите целые числа через пробел: ')
number = int(input('Введите число: '))
sequence1 = sequence.replace(' ', '')
if sequence1.isdigit() is False:
    print('Ошибка.Введите целые числа')
else:
    sequence= sequence.split()
    int_lst = int_lst = [int(x) for x in sequence]
    print("Список:", int_lst)

for i in range(len(int_lst)):
    for j in range(len(int_lst) - i - 1):
        if int_lst[j] > int_lst[j + 1]:
            int_lst[j], int_lst[j + 1] = int_lst[j + 1], int_lst[j]


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'
print(f'Список по возрастанию: {int_lst}')

if not binary_search(int_lst, number, 0, len(int_lst)):
    rI = min(int_lst, key=lambda x: (abs(x - number), x))
    ind = int_lst.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < number:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {int_lst[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {int_lst.index(rI)}
В списке нет меньшего элемента''')
    elif rI > number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {int_lst.index(rI)}
Ближайший меньший элемент: {int_lst[min_ind]} его индекс: {min_ind}''')
    elif int_lst.index(rI) == 0:
        print(f'Индекс введенного элемента: {int_lst.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(lint_lst, number, 0, len(int_lst))}')
