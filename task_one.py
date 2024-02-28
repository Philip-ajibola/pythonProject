#list1 = [10,2,8,9,3,4,1,5]

def sort_in_ascending_order(list1):
    for number in range(len(list1)):
        for numbers in range(number+1,len(list1)):
            if list1[number] > list1[numbers]:
                temp = list1[numbers]
                list1[numbers] = list1[number]
                list1[number] = temp
    return list1

list1 = [10,2,8,9,3,4,1,5]
#print(sort_in_ascending_order(list1))
