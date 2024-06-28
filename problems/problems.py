import json
file_path = 'problems.json'

def load_problems():
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data

# def sum_cars(cars):
#     return print("sum of cars")

# def total_profit(cars):
#     return print("total of profit")

