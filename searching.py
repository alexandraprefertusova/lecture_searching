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


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


if __name__ == "__main__":
    main()
