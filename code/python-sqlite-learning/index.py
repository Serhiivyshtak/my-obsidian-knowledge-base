from SecundariesApp import SecundariesApp

try:
    secundariesApp = SecundariesApp("database.db")
except RuntimeError as error:
    print(f"RUNTIME ERROR -> {error}")
    exit()

available_actions = secundariesApp.available_actions

print("Hello and welcome to Secundaries management system. Type in a number representing your desired action")

while True:
    for action in available_actions:
        print(f"{available_actions.index(action) + 1}. {action.get("description")}")
    
    print("---")

    try:
        desired_action = int(input("Your desired action: "))
        print("---")
    except ValueError:
        print("Invalid input. Only digits allowed")
        continue

    if desired_action not in range(1, len(available_actions) + 1):
        print(f"Invalid input. There is no action represented by the number {desired_action}")
        continue

    available_actions[desired_action - 1].get("func")()

    print("---")
