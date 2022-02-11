while True:

    # Get fuel remaining in the tank from the user
    fuel_tank = input("Enter fuel remaining:")
    fuel_tank = float(fuel_tank)

    # Get L/100km used from the user
    fuel = input("Enter car's L/18kmh:")
    fuel = float(fuel)

    # Get distance driven from the user
    distance = input("Enter kilometers driven:")
    distance = float(distance)

    # Get speed used from the user
    speed = input("Enter driving speed:")
    speed = float(speed)

    # Calculate and print the answer
    time = distance / speed
    fuel_burned = distance / 100 * fuel
    fuel_remaining = fuel_tank - fuel_burned

    hours = int(time)
    minutes_remainder = (time - hours) * 60
    minutes = int(minutes_remainder)

    print("-----------------------------------------")
    print("Time traveled: ", hours, "h:", minutes, "min")
    print("Fuel burned: ", fuel_burned, " liters")
    print("==========================================")
    print("Fuel remaining: ", fuel_remaining, " liters")
    print("==========================================")

    again = input("Go again? (y/n)")
    if again == "n":
        break
