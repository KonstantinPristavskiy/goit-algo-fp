import heapq

def dijkstra(graph, start_vertex):
    """
    Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів
    у зваженому графі від початкової вершини.

    :param graph: Словник, що представляє граф (списки суміжності).
    :param start_vertex: Початкова вершина.
    :return: Словник з найкоротшими відстанями до кожної вершини.
    """
    # Ініціалізація відстаней. Усі відстані нескінченні, крім початкової.
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    # Бінарна купа (пріоритетна черга) для зберігання вершин для відвідування.
    # Зберігаємо кортежі (відстань, вершина).
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        # Отримуємо вершину з найменшою відстанню з купи
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдений шлях довший за вже відомий, ігноруємо його
        if current_distance > distances[current_vertex]:
            continue

        # Ітеруємо по сусідах поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Додаємо сусіда в купу з новою відстанню
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
if __name__ == "__main__":
    # Створення зваженого графа у вигляді списків суміжності
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1, 'E': 3},
        'E': {'D': 3}
    }

    # Визначення початкової вершини
    start_node = 'A'

    # Виклик функції для обчислення найкоротших шляхів
    shortest_distances = dijkstra(graph, start_node)

    # Виведення результатів
    print(f"Найкоротші шляхи від вершини '{start_node}':")
    for vertex, distance in shortest_distances.items():
        print(f"  До вершини {vertex}: {distance}")
