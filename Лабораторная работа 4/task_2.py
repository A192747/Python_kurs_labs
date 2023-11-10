# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


# TODO считать содержимое csv файла
# TODO Сериализовать в файл с отступами равными 4
def task() -> None:
    with open(OUTPUT_FILENAME, 'w') as file_out:
        with open(INPUT_FILENAME, 'r') as file_in:
            reader = csv.DictReader(file_in)
            json_data = [row for row in reader]
            json.dump(json_data, file_out, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
