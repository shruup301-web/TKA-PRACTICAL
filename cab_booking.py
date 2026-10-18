import random

print("Welcome to Cab Booking Chatbot")

while True:
    print("\n1. Book a Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nSelect Cab Type")
        print("1. Auto")
        print("2. Sedan")
        print("3. SUV")

        cab = input("Enter cab choice: ")

        if cab == "1":
            rate = 12
            cab_name = "Auto"
        elif cab == "2":
            rate = 18
            cab_name = "Sedan"
        elif cab == "3":
            rate = 25
            cab_name = "SUV"
        else:
            print("Invalid cab choice")
            continue

        print("\nSelect Route")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")

        route = input("Enter route choice: ")

        if route == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice")
            continue

        fare = distance * rate

        print("\n----- Booking Details -----")
        print("Cab Type:", cab_name)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate per km: Rs.", rate)
        print("Total Fare: Rs.", fare)

        print("\n1. Confirm and Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter your choice: ")

        if confirm == "1":
            otp = random.randint(1000, 9999)
            print("Booking Confirmed!")
            print("Your OTP is:", otp)
            print("Ride cannot be cancelled now.")

        elif confirm == "2":
            print("Your ride has been cancelled.")

        else:
            print("Invalid choice. Booking not confirmed.")

    elif choice == "2":
        print("Thank you for using Cab Booking Chatbot!")
        break

    else:
        print("Invalid choice. Please try again.")