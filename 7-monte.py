import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    results = [0] * 13  # Можливі суми від 2 до 12 (індекси 2-12)
    
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        sum_rolls = roll1 + roll2
        results[sum_rolls] += 1

    return results

def calculate_probabilities(results, num_rolls):
    probabilities = [(count / num_rolls) * 100 for count in results]
    return probabilities

def plot_probabilities(probabilities):
    sums = list(range(2, 13))
    plt.bar(sums, probabilities[2:], tick_label=sums)
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

def main():
    num_rolls = 1000000  # Кількість кидків кубиків
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)

    print("Сума | Імовірність (%)")
    print("----------------------")
    for sum_value in range(2, 13):
        print(f"{sum_value:4} | {probabilities[sum_value]:.2f}%")

    plot_probabilities(probabilities)

    analytical_probabilities = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    with open('readme7.md', 'w', encoding='utf-8') as f:
        f.write("# Висновки\n\n")
        f.write("## Результати симуляції\n\n")
        f.write("Імовірності сум при киданні двох кубиків, отримані методом Монте-Карло:\n\n")
        f.write("| Сума | Імовірність (%) |\n")
        f.write("|------|-----------------|\n")
        for sum_value in range(2, 13):
            f.write(f"| {sum_value:4} | {probabilities[sum_value]:.2f} |\n")

        f.write("\n## Порівняння з аналітичними результатами\n\n")
        f.write("| Сума | Аналітична імовірність (%) | Монте-Карло імовірність (%) |\n")
        f.write("|------|----------------------------|-----------------------------|\n")
        for sum_value in range(2, 13):
            f.write(f"| {sum_value:4} | {analytical_probabilities[sum_value]:.2f} | {probabilities[sum_value]:.2f} |\n")

        f.write("\n## Висновок\n\n")
        f.write("Метод Монте-Карло показав результати, що добре узгоджуються з аналітичними розрахунками. Різниця в імовірностях може бути зменшена збільшенням кількості симуляцій.\n")

if __name__ == "__main__":
    main()