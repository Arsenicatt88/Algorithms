graf = {
    "Василеостровская": {"Гостинный двор": 4},
    "Гостинный двор": {"Василеостровская": 4, "Невский проспект": 1, "Маяковская": 4},
    "Маяковская": {"Гостинный двор": 4, "Площадь восстания": 1, "Площадь Александра Невского": 4},
    "Лиговский проспект": {"Площадь Александра Невского": 2, "Достоевская": 2},
    "Адмиралтейская": {"Садовая": 5},
    "Садовая": {"Адмиралтейская": 5, "Спасская": 1, "Сенная площадь": 1, "Звенигородская": 5},
    "Звенигородская": {"Садовая": 5, "Пушкинская": 1, "Обводный канал": 5},
    "Обводный канал": {"Звенигородская": 5},
    "Невский проспект": {"Гостинный двор": 1, "Сенная площадь": 6},
    "Сенная площадь": {"Спасская": 1, "Садовая": 1, "Технологический институт": 6, "Невский проспект": 6},
    "Технологический институт": {"Пушкинская": 4, "Сенная площадь": 6},
    "Площадь восстания": {"Маяковская": 1, "Владимирская": 3},
    "Владимирская": {"Достоевская": 1, "Пушкинская": 3, "Площадь восстания": 3},
    "Пушкинская": {"Звенигородская": 1, "Технологический институт": 3, "Владимирская": 3},
    "Спасская": {"Садовая": 1, "Сенная площадь": 1, "Достоевская": 2},
    "Площадь Александра Невского": {"Лиговский проспект": 2, "Новочеркасская": 2},
    "Новочеркасская": {"Площадь Александра Невского": 2, "Ладожская": 2},
    "Ладожская": {"Новочеркасская": 2, "Проспект большевиков": 2},
    "Проспект большевиков": {"Ладожская": 2},
    "Достоевская": {"Спасская": 2, "Владимирская": 1, "Лиговский проспект": 2}
}


def calculate_path_time(graph, path):
    if not path or len(path) < 2:
        return 0
    total_time = 0
    for i in range(len(path) - 1):
        total_time += graph[path[i]][path[i + 1]]
    return total_time


def bfs(graph, start, end):
    queue = [[start]]
    visited = {start}
    head = 0

    while head < len(queue):
        path = queue[head]
        head += 1
        node = path[-1]

        if node == end:
            total_time = calculate_path_time(graph, path)
            return path, total_time

        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None, 0


def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == end:
        total_time = calculate_path_time(graph, path)
        return path, total_time

    for neighbor in graph.get(start, {}):
        if neighbor not in visited:
            result_path, result_time = dfs(graph, neighbor, end, visited, path)
            if result_path:
                return result_path, result_time

    path.pop()
    return None, 0


# Тест 1
print("_____________________________________________")
p, t = bfs(graf, "Василеостровская", "Достоевская")
print(f"BFS: {p} | Время: {t} мин")
p, t = dfs(graf, "Василеостровская", "Достоевская")
print(f"DFS: {p} | Время: {t} мин")
print("_____________________________________________")

# Тест 2
p, t = bfs(graf, "Новочеркасская", "Садовая")
print(f"BFS: {p} | Время: {t} мин")
p, t = dfs(graf, "Новочеркасская", "Садовая")
print(f"DFS: {p} | Время: {t} мин")
print("_____________________________________________")

# Тест 3
p, t = bfs(graf, "Лиговский проспект", "Гостинный двор")
print(f"BFS: {p} | Время: {t} мин")
p, t = dfs(graf, "Лиговский проспект", "Гостинный двор")
print(f"DFS: {p} | Время: {t} мин")
print("_____________________________________________")