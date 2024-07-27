def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)

    return selected_items, total_calories

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = item_names[i - 1]
            selected_items.append(item)
            w -= items[item]['cost']

    return selected_items, total_calories

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 115

# Використання жадібного алгоритму
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(f"Обрані страви (жадібний алгоритм): {selected_items_greedy}")
print(f"Сумарна калорійність: {total_calories_greedy}")

# Використання алгоритму динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print(f"Обрані страви (динамічне програмування): {selected_items_dp}")
print(f"Сумарна калорійність: {total_calories_dp}")