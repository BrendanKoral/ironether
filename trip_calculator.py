city = input("Choose a city: Charlotte, Tampa, Pittsburgh, or Los Angeles: ")

days = int(input("Enter number of days for the trip: "))

spending_money = int(input("Enter your desired amount of spending money: "))

def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 20
    return cost
    
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print("The total cost of your trip is: $" + str(trip_cost(city, days, spending_money)))