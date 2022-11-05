clients = int(input("Enter the number of clients you have: "))
scoop_price = 10

for client in range(clients):
    scoops_list = {
        "brown": {"discount": 5, "quantity": 0},
        "white": {"discount": 2, "quantity": 0},
        "green": {"discount": 4, "quantity": 0},
        "red": {"discount": 1, "quantity": 0},
    }

    print(f"\nClient {client + 1}:")
    scoops = int(input("Enter the number of scoops you would like: "))

    price = 0
    discount = 0
    for scoop in range(scoops):
        scoop_available = False
        while not scoop_available:
            scoop_color = input(f"Enter the color of scoop {scoop + 1} (brown/ white/ green/ red): ")

            if scoop_color in scoops_list:
                price += scoop_price
                discount += scoops_list[scoop_color]["discount"]
                scoops_list[scoop_color]["quantity"] += 1
                scoop_available = True
            else:
                print("This color is unavailable! try again.\n")

    print(f"\nNumber of scoops: {scoops}\nPrice before discount: {price}\nPrice after discount: {price - discount}\n"
          f"Scoops colors list:")
    for color in scoops_list:
        print(f"\t{color.title()}: {scoops_list[color]['quantity']}")
