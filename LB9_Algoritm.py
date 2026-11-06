import heapq
def select_activities(activities):
    # Сортируем по времени окончания, затем по началу
    sorted_activities = sorted(activities, key=lambda x: (x[1], x[0]))
    
    selected = []
    last_end = float("-inf")
    
    for start, end in sorted_activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected


activities = [(3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14),(1, 4)]

print(select_activities(activities))


def min_cable_cost(lengths):
    if len(lengths) <= 1:
        return 0
    
    heap = lengths[:]
    heapq.heapify(heap)
    
    total_cost = 0
    
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        heapq.heappush(heap, cost)
    
    return total_cost


lengths = [4, 3, 2, 6]
print(min_cable_cost(lengths))

def place_towers(cities, radius):
    cities = sorted(cities)
    towers = []
    i = 0
    n = len(cities)
    
    while i < n:

        tower_pos = cities[i] + radius
        towers.append(tower_pos)
        
        i += 1
        while i < n and cities[i] <= tower_pos + radius:
            i += 1
    
    return len(towers), towers


cities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
radius = 2

count, positions = place_towers(cities, radius)
print("Количество вышек: ",count)
print("Позиции: ",positions)