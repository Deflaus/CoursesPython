stats = {'facebook': 55, 'yandex': 120, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
maximum = max(stats.values())
max_stats = []
for canal in stats:
    if stats.get(canal) == maximum:
        max_stats.append(canal)

print("Каналы с максимальным объемом:")
for stat in max_stats:
    print(stat, end=" ")
