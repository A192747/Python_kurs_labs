# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants_2, split_elem =','):
    set_1 = set(participants1.split(split_elem))
    set_2 = set(participants_2.split(split_elem))
    result_list = list(set_1.intersection(set_2))
    result_list.sort()
    return result_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

# проверка с разделителем по умолчанию
print(find_common_participants(participants_first_group, participants_second_group))

# проверка с заданным разделителем
print(find_common_participants(participants_first_group, participants_second_group, "|"))
