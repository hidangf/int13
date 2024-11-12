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
