from pathlib import Path
import json


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

def main():
    ordered_data = read_data("sequential.json", "ordered_numbers")

    target = 5

    index = binary_search(ordered_data, target)

    print("Seřazená data:", ordered_data)
    print("Hledané číslo:", target)
    print("Výsledek (index):", index)


if __name__ == "__main__":
    main()
