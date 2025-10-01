import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    """Simulates rolling two dice for a given number of rolls."""
    sums_counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sums_counts[roll_sum] += 1
    return sums_counts

def calculate_probabilities(sums_counts, num_rolls):
    """Calculates the probabilities of each sum."""
    probabilities = {}
    for sum_val, count in sums_counts.items():
        probabilities[sum_val] = (count / num_rolls) * 100
    return probabilities

def print_results_table(probabilities):
    """Prints the results in a formatted table."""
    print("Сума\tІмовірність (%)")
    for sum_val, prob in sorted(probabilities.items()):
        print(f"{sum_val}\t{prob:.2f}%")

def plot_probabilities(probabilities):
    """Plots the probabilities of the sums."""
    sums = sorted(probabilities.keys())
    probs = [probabilities[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.grid(axis='y', linestyle='--')
    plt.show()

if __name__ == "__main__":
    num_rolls = 1000000  # Велика кількість кидків
    
    # Виконання симуляції
    counts = simulate_dice_rolls(num_rolls)
    
    # Обчислення ймовірностей
    probabilities = calculate_probabilities(counts, num_rolls)
    
    # Виведення результатів у вигляді таблиці
    print_results_table(probabilities)
    
    # Відображення графіка
    plot_probabilities(probabilities)
