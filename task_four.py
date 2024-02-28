
def separate_sentence_and_count_number_of_occurrence(sentence):
    my_dict = {}
    my_list = list(sentence.split(" "))
    for word in my_list:
        frequency = 0
        for index in range(len(my_list)):
            if word == my_list[index]:
                frequency += 1
            my_dict[word] = frequency
    return my_dict


sentence = "the palace is few miles away from the village but going to the palace to see startups is cool fun"
print(separate_sentence_and_count_number_of_occurrence(sentence))