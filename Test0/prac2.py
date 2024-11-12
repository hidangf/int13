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

