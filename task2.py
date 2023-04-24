def task1():
    day = int(input("input day: "))
    month = input("input month: ")
    temperature = int(input('input temperature: '))

    print("Сегодня %.d %s На улице %.d градусов." % (day, month, temperature))
    if temperature < 0:
        print("Холодно, лучше остаться дома.")


def task2():
    speed_kmh = 1079252848.8 // 3600
    print("Скорость света равна %.d км/ч" % speed_kmh)


def task3():
    product_list = ["Ананасы", "Яблоки", "Груши"]
    count_ = len(product_list)
    print("У тебя %.d продуктов, где %.d — значение переменной count." % (count_, count_))
    return product_list


def task4(arr):
    for el in arr:
        print(el, end=' ')
    print()


def task5(arr):
    for el in arr:
        if len(el) % 2 == 0:
            print(el, end=' ')
    print()


def task6(curr):
    value = 0
    i = 2
    curr_sqrt = curr * 0.5 + 1 # берем на 1 больше, чтобы не потерять целый корень, если он является делителем

    while (value == 0) and (curr_sqrt > i):
        if curr % i == 0:
            value += 1
        i += 1

    if value == 1:
        print("Составное")
    else:
        print("Простое")


def task7(n):
    arr = [1, 1]
    if n < 2:
        print(arr[n])
    else:
        for i in range(1, n):
            arr.append(arr[i] + arr[i-1])
        print(arr[n])


# print("-----ТЕСТЫ-----")
# task1()
# task2()
# arr = task3()
# task4(arr)
# task5(arr)
# test = [2, 10, 11]
# for el in test:
#     task6(el)
# task7(5)
