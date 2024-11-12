def my_code(data, i=0):
    for key, value in data.items():
        print('\t' * i + str(key) + ':')
        if isinstance(value, dict):
            my_code(value, i + 1)
        else:
            print('\t'* (i + 1) + str(value))
print('Тест 0. Тест из ТЗ\n')
data_0 = {
    '1': {'child': '1/child/value'},
    '2': '2/value'
}
my_code(data_0)
print('Тест 1. Вложенный словарь\n')
data_1 = {
    'A': {'B': {'C': 'A/B/C Value'}},
    'X': 'X Value'
}
my_code(data_1)

print('Тест 2: Пустой словарь\n')
data_2 = {}
my_code(data_2)
print('Тест 3: Словарь с несколькими уровнями вложенности и разными типами данных\n')
data_3 = {
    'level1': {
        'level2_a': {
            'level3': 'deep_value'
        },
        'level2_b': 42
    },
    'another_key': {
        'another_dict': {
            'new_key': [1, 2, 3]
        }
    }
}
my_code(data_3)
print('Тест 4: Смешанные типы данных\n')
data_4 = {
    'string': 'PT',
    'integer': 123,
    'list': [1, 2, 3],
    'dict': {
        'key': 'value'
    }
}
my_code(data_4)

print('Тест 5: Несколько ключей на одном уровне\n')
data_5 = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}
my_code(data_5)

