# TODO  Напишите функцию count_letters

def count_letters(text):
    lower_text = text.lower()
    result_dict = dict()
    for elem in lower_text:
        if elem.isalpha() and elem not in result_dict:
            result_dict.update({elem: lower_text.count(elem)})
    return result_dict


# TODO Напишите функцию calculate_frequency

def calculate_frequency(dict_):
    all_letters_count = sum(dict_.values())

    for letter, count in dict_.items():
        dict_[letter] = round(count / all_letters_count, 2)
    return dict_


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

for letter, value in calculate_frequency(count_letters(main_str)).items():
    print(f"{letter}: {value:.2f}")
# TODO Распечатайте в столбик букву и её частоту в тексте
