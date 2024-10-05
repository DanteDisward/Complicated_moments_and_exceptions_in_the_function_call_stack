def personal_sum(numbers):
    sum_num = 0
    incorrect_data = 0
    for num in numbers:
        try:
            sum_num += num
        except TypeError:
            incorrect_data += 1
    result = (sum_num, incorrect_data)
    return result


def calculate_average(numbers):
    try:
        s = personal_sum(numbers)
        result = s[0] / (len(numbers) - s[1])
    except ZeroDivisionError:
        result = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        result = None
    return result


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
