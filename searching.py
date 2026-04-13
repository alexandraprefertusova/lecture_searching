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

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")

    target = 5

    result = linear_search(sequential_data, target)

    print("Data:", sequential_data)
    print("Hladane cislo:", target)
    print("Pozicia:", result["positions"])
    print("Pocet vyskytov:", result["count"])


if __name__ == "__main__":
    main()
