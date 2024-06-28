import json

from problems.problems_menu import problems_menu

file_path = 'cars.json'

def load_cars():
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data

def get_cars(cars):
    for car in cars:
        print(car)

def add_car(cars):
    problems_menu(cars)
    new_number = input("Enter car number: ")
    new_problem = input("Enter car problem : ")

    new_car = {"car_number": new_number, "problem": new_problem}
    cars.append(new_car)
    return print("New car added ", new_car)

def delete_car(cars:list):
    car_select = int(input("choose car number: "))
    cars.pop(car_select)
    return print("car deleted")

def search_car(cars):
    search_str = input("Please enter search str: ")
    found = False
    for car in cars:
        if (
            search_str.lower() in str(car["car_number"]).lower() 
            or search_str.lower() in car["problem"].lower()
        ):
            print(car["car_number"],car["problem"])
            found = True
            return

    if not found:
        print("Not found!")



