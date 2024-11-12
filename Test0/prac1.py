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

