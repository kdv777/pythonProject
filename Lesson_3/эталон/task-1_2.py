# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# num_translate("one")
# "один"
# num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

# 2.* Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы. Например:
# num_translate_adv("One")
# "Один"
# num_translate_adv("two")
# "два"


eng_rus = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять", }


def num_translate(word, dictionary):
    # Можно было использовать метод get. Тогда без проверки
    if word in dictionary.keys(): 
        return dictionary[word]


# Ключи словаря записаны в нижнем регистре и дублировать их для заглавной буквы - плохо.
def num_translate_adv(word, dictionary):
    word_lower = word.lower()
    if word_lower in dictionary.keys():
        # Первая буква - заглавная. Можно использовать str.istitle
        if 65 <= ord(word[0]) <= 90:  
            return dictionary[word_lower].title()
        return dictionary[word_lower]


print(num_translate("one", eng_rus))
print(num_translate("six", eng_rus))
print(num_translate("Six", eng_rus))

print(num_translate_adv("one", eng_rus))
print(num_translate_adv("six", eng_rus))
print(num_translate_adv("Six", eng_rus))
