from cars.actions import get_cars, add_car, delete_car, search_car



def menu_selection(cars,choice):
    if choice == "1":
        return get_cars(cars)
    elif choice == "2":
        return add_car(cars)
    elif choice == "3":
        return delete_car(cars)
    elif choice == "4":
        return search_car(cars)
    elif choice == "5":
        print("exit")
        exit()