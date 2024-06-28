# from problems.problems import sum_cars, total_profit
from cars.menu import menu_selection
from cars.actions import load_cars

# print(f"Currently there are {sum_cars} cars. The current profit is: {total_profit}")
try:
    def menu(cars):
        while True:
            print("Choose one of the following actions: ")
            print("1 - List all cars")
            print("2 - Add a car")
            print("3 - Delete a car")
            print("4 - Search a car") # printing 'car_number' continue later
            print("5 - Exit")
            choice = input("")
            menu_selection(cars,choice)

    def main():
        cars = load_cars();
        menu(cars)

    if __name__ == "__main__":
        main()




except Exception as err:
    print(err)

