def query(events: list, assets: list) -> list:
    asset_d = {asset[0]: asset[1] for asset in assets}
    result = []
    for event in events:
        event_id, event_date, event_name, asset_id = event
        asset_name = asset_d.get(asset_id, None)
        result.append([event_id, event_name, asset_id, asset_name])

    result.sort(key=lambda x: x[0])
    return result[:100]
print('Тест 0. Тест из ТЗ.\n')
events0 = [
    [4, '2024-03-28', 'Event 4', 1],
    [1, '2024-03-26', 'Event 1', 1],
    [6, '2024-03-29', 'Event 6', 3],
    [3, '2024-03-28', 'Event 3', 2],
    [5, '2024-03-29', 'Event 5', None],
    [2, '2024-03-27', 'Event 2', None]
]

assets0 = [
    [4, 'Asset 4'],
    [1, 'Asset 1'],
    [3, 'Asset 3'],
    [2, 'Asset 2']
]

result_0 = query(events0, assets0)
for row in result_0:
    print(row)

print('Тест 1: Совпадение всех `asset_id` с `assets`\n')
events1 = [
    [1, '2024-03-26', 'Event 1', 1],
    [2, '2024-03-27', 'Event 2', 2],
    [3, '2024-03-28', 'Event 3', 3],
    [4, '2024-03-29', 'Event 4', 4]
]

assets1 = [
    [1, 'Asset 1'],
    [2, 'Asset 2'],
    [3, 'Asset 3'],
    [4, 'Asset 4']
]

result_1 = query(events1, assets1)
for row in result_1:
    print(row)

print('Тест 2: Некоторые `asset_id` отсутствуют в `assets`\n')
events2 = [
    [1, '2024-03-26', 'Event 1', 1],
    [2, '2024-03-27', 'Event 2', None],
    [3, '2024-03-28', 'Event 3', 3],
    [4, '2024-03-29', 'Event 4', 5]
]

assets2 = [
    [1, 'Asset 1'],
    [3, 'Asset 3']
]

result_2 = query(events2, assets2)
for row in result_2:
    print(row)

print('Тест 3: `events` отсортированы не по `event_id`\n')
events3 = [
    [4, '2024-03-29', 'Event 4', 4],
    [1, '2024-03-26', 'Event 1', 1],
    [3, '2024-03-28', 'Event 3', 3],
    [2, '2024-03-27', 'Event 2', 2]
]

assets3 = [
    [1, 'Asset 1'],
    [2, 'Asset 2'],
    [3, 'Asset 3'],
    [4, 'Asset 4']
]

result_3 = query(events3, assets3)
for row in result_3:
    print(row)

print('Тест 4: Пустой список `events`\n')
events4 = []
assets4 = [
    [1, 'Asset 1'],
    [2, 'Asset 2']
]

result_4 = query(events4, assets4)
print(result_4)

print('Тест 5: Пустой список `assets`\n')
events5 = [
    [1, '2024-03-26', 'Event 1', 1],
    [2, '2024-03-27', 'Event 2', None]
]

assets5 = []

result_5 = query(events5, assets5)
for row in result_5:
    print(row)
