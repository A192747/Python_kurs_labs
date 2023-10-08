numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

elem_index = numbers.index(None)
insert_value = sum(numbers[:elem_index] + numbers[elem_index + 1:]) / len(numbers)

numbers[elem_index] = insert_value

print("Измененный список:", numbers)
