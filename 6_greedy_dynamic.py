items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Додаємо співвідношення калорій до вартості для кожного предмету
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    chosen_items = []
    total_calories = 0
    total_cost = 0

    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            chosen_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost = data['cost']
        calories = data['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення набору предметів
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, data = item_list[i - 1]
            chosen_items.append(name)
            w -= data['cost']

    return chosen_items, dp[n][budget]

budget = 100
greedy_choice, greedy_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Chosen items:", greedy_choice)
print("Total calories:", greedy_calories)

print("\n" + "="*30 + "\n")

dp_choice, dp_calories = dynamic_programming(items, budget)
print("Dynamic Programming:")
print("Chosen items:", dp_choice)
print("Total calories:", dp_calories)
