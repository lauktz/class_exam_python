
problems = [
    {"Problem": "Engine", "Price": 2000},
    {"Problem": "Breaks", "Price": 1000},
    {"Problem": "5000 km treatment", "Price": 500},
    {"Problem": "10,000 km treatment", "Price": 1000},
    {"Problem": "Filters + Oil", "Price": 250},
    {"Problem": "Gear", "Price": 1000}

]


def problems_menu(cars):
            from cars.actions import add_car
            while True:
                print("Choose a problem form the list: ")
                print("0 - ",problems[0]["Problem"])
                print("1 - ",problems[1]["Problem"])
                print("2 - ",problems[2]["Problem"])
                print("3 - ",problems[3]["Problem"])
                print("4 - ",problems[4]["Problem"])
                print("5 - ",problems[5]["Problem"])
                choice = int(input(""))
                print(f'The price of this fix is: {problems[choice]["Price"]} NIS. do you wish to proceed? yes/no')
                user_decision = input()
                if user_decision == "yes":
                        add_car(cars)
                        break
                elif user_decision == "no":
                        print("Thank you, see you next time!")
                        break




        # print("test 1 - Engine")
        # print("test 2 - Breaks")
        # print("test 3 - 5000 km treatment")
        # print("test 4 - Filters + Oil")
        # print("test 5 - Gear")
        # choice = input("")