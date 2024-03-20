def count_number_occurrence(numbers):
    for number in numbers:
        num = numbers.count(number)
        if num > 1:
            return [num, number]


def count_number_occurrence2(numbers):
    return map(filter(lambda number: [numbers.count(number) > 1, number], numbers))


list1 = [1, 2, 3, 4, 2, 2]
print(count_number_occurrence2(list1))
