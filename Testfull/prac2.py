def my_code(data, start):
    if start not in data:
        return
    visited = set()
    def dfs(node):
        print(node, end='\n')
        visited.add(node)
        for neighbor in data.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)
print('Тест 0. Тест из ТЗ')
data_0 = {
    1: [2, 3],
    2: [3, 4],
    4: [1]
}
my_code(data_0, 1)
print('Тест 1. Граф с циклом и несколькими ветвлениями\n')
data_1 = {
    1: [2, 3],
    2: [3, 4, 5],
    3: [6],
    4: [1, 7],
    7: [8]
}
my_code(data_1, 1)

print('Тест 2: Линейный граф\n')
data_2 = {
    1: [2],
    2: [3],
    3: [4],
    4: [5]
}
my_code(data_2, 1)

print('Тест 3: Дерево\n')
data_3 = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
}
my_code(data_3, 1)


print('Тест 4: Независимые подграфы\n')
data_4 = {
    1: [2],
    2: [3],
    4: [5]
}
print('Запуск с первой компоненты(для первого подграфа)\n')
my_code(data_4, 1)
print("\n")
print('Запуск со второй(с 4)(для второго подграфа)\n')
my_code(data_4, 4)
print("\n")

print('Тест 5: Пустой граф')
data_5 = {}
my_code(data_5, 1)

