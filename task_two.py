def sort_in_ascending_order(list1):
    for number in range(len(list1)):
        for numbers in range(number+1,len(list1)):
            if list1[number] < list1[numbers]:
              list1[number],list1[numbers] = list1[numbers], list1[number]
    return list1


list1 = [10, 2, 8, 9, 3, 4, 1, 5]
print(sort_in_ascending_order(list1))


def check_index(list1,number1):
    for number in range(len(list1)):
        if number1 == list1[number]:
            return f"{number1} is in index {number}"

    return f"{number1} is not present in the list"


list2 = [5, 6, 7, 8, 9, 10, 15]
check = 17
print(check_index(list2,check))

