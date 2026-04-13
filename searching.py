import json
import random
import time
import matplotlib.pyplot as plt



def read_data(filename, field):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        if field not in data:
            return None

        return data[field]

    except (FileNotFoundError, json.JSONDecodeError):
        return None



def linear_search(sequence, target):
    positions = []

    for index, value in enumerate(sequence):
        if value == target:
            positions.append(index)

    return {
        "positions": positions,
        "count": len(positions)
    }


def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def generate_data(size):
    data = [random.randint(0, size) for _ in range(size)]
    return data, sorted(data)



def measure_time(func, data, target, repeats=5):
    total_time = 0

    for _ in range(repeats):
        start = time.perf_counter()
        func(data, target)
        end = time.perf_counter()
        total_time += (end - start)

    return total_time / repeats

def pattern_search(sequence, pattern):
    positions = set()
    m = len(pattern)
    n = len(sequence)

    for i in range(n - m + 1):

        if sequence[i:i + m] == pattern:
            positions.add(i)

    return positions



def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    ordered_data = read_data("sequential.json", "ordered_numbers")

    target = 5

    print("=== TEST FUNKCÍ ===")
    print("Data:", sequential_data)

    linear_result = linear_search(sequential_data, target)
    print("Linear search:", linear_result)

    binary_result = binary_search(ordered_data, target)
    print("Binary search index:", binary_result)


    sizes = [100, 500, 1000, 2000]

    linear_times = []
    binary_times = []
    set_times = []

    for size in sizes:
        data, ordered = generate_data(size)
        target = data[-1]

        data_set = set(data)

        linear_times.append(measure_time(linear_search, data, target))
        binary_times.append(measure_time(binary_search, ordered, target))
        set_times.append(measure_time(lambda s, t: t in s, data_set, target))

    plt.plot(sizes, linear_times, label="Linear search")
    plt.plot(sizes, binary_times, label="Binary search")
    plt.plot(sizes, set_times, label="Set membership")

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas (s)")
    plt.title("Porovnání vyhledávacích algoritmů")
    plt.legend()
    plt.grid()

    plt.savefig("graf.png")
    plt.show()

    dna_sequence = read_data("sequential.json", "dna_sequence")
    pattern = "ATA"
    result = pattern_search(dna_sequence, pattern)
    print("DNA sekvence:", dna_sequence)
    print("Vzor:", pattern)
    print("Pozice výskytu:", result)



if __name__ == "__main__":
    main()