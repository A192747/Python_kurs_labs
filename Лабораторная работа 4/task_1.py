# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    return round(sum([pair['score'] * pair['weight'] for pair in data]), 3)


print(task())
