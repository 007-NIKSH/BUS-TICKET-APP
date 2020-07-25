Route_1 = ['Bangalore', 'Hyderabad', '1798']
Route_2 = ['Chennai', 'Bangalore', '1448']
Route_3 = ['Chennai', 'Kochi', '2728']
Route_4 = ['Pune', 'Mumbai', '653']
Route_5 = ['Mumbai', 'Delhi', '3259']
Passengers = []
Seates = []
Booked_Seates = [7, 1, 20, 5, 6]
Age = []
Fare = 0

Tru1 = False
Try2 = False

def Bus():
  print("""
   ____________________________
  |                       ___  |
  |                      |   | |
  |                      |___| |
  |____________     ___________|
  |   ___   ___     ___   ___  |
  |  | 1 | | 2 |   | 3 | | 4 | |
  |  |_ _| |_ _|   |___| |___| |
  |   ___   ___     ___   ___  |
  |  | 5 | | 6 |   | 7 | | 8 | |
  |  |___| |___|   |___| |___| |
  |   ___   ___     ___   ___  |
  |  | 9 | | 10|   | 11| | 12| |
  |  |___| |___|   |___| |___| |
  |   ___   ___     ___   ___  |
  |  | 13| | 14|   | 15| | 16| |
  |  |___| |___|   |___| |___| |
  |   ___   ___     ___   ___  |
  |  | 17| | 18|   | 19| | 20| |
  |  |___| |___|   |___| |___| |
  |____________________________|""")
  print(f'\nBooked Seats: {Booked_Seates}')

print(f'\nRoute 1: {Route_1[0]} - {Route_1[1]}'),
print(f'Fare: ₹ {Route_1[2]}'),

print(f'\nRoute 2: {Route_2[0]} - {Route_2[1]}'),
print(f'Fare: ₹ {Route_2[2]}'),

print(f'\nRoute 3: {Route_3[0]} - {Route_3[1]}'),
print(f'Fare: ₹ {Route_3[2]}'),

print(f'\nRoute 4: {Route_4[0]} - {Route_4[1]}'),
print(f'Fare: ₹ {Route_4[2]}'),

print(f'\nRoute 5: {Route_5[0]} - {Route_5[1]}'),
print(f'Fare: ₹ {Route_5[2]}')

R = int(input("\nEnter Route Number: "))
print("\n")
Try1 = True

while Try1 == True:
  if R == 1:
    Current_Route = Route_1
    print(f'\nCurrent Route: {Current_Route[0]} - {Current_Route[1]}'),
    print(f'Fare: ₹ {Current_Route[2]}')
    Try2 = True
    break

  elif R == 2:
    Current_Route = Route_2
    print(f'\nCurrent Route: {Current_Route[0]} - {Current_Route[1]}'),
    print(f'Fare: ₹ {Current_Route[2]}')
    Try2 = True
    break

  elif R == 3:
    Current_Route = Route_3
    print(f'\nCurrent Route: {Current_Route[0]} - {Current_Route[1]}'),
    print(f'Fare: ₹ {Current_Route[2]}')
    Try2 = True
    break

  elif R == 4:
    Current_Route = Route_4
    print(f'\nCurrent Route: {Current_Route[0]} - {Current_Route[1]}'),
    print(f'Fare: ₹ {Current_Route[2]}')
    Try2 = True
    break

  elif R == 5:
    Current_Route = Route_5
    print(f'\nCurrent Route: {Current_Route[0]} - {Current_Route[1]}'),
    print(f'Fare: ₹ {Current_Route[2]}')
    Try2 = True
    break

  else:
    print("Invalid Route")
    break

while Try2 == True:
  print("\n1 - View Passengers")
  print("2 - View Cost")
  print("3 - View Booked Seats")
  print("4 - Add Passenger")
  print("5 - Conform Tickets")
  print("6 - Exit")
  Option1 = int(input("\nOption: "))

  if Option1 == 1:
    print(f'\nPassengers: {Passengers}')
    continue

  elif Option1 == 2:
    print(f'\nCost: {Fare}') 
  
  elif Option1 == 3:
    print(f'\nSeats: {Seates}') 

  elif Option1 == 4:
    print("\nPassengers Details: ")
    A = input("Name: ")
    B = int(input("Age: "))
    Bus()
    D = int(input("Seat: "))
        
    if D not in Booked_Seates:
        Passengers.append(A)
        Age.append(B)
        Seates.append(D)
        Booked_Seates.append(D)
        
        if B <= 10:
            Fare += 0
            continue

        else:
            F = int(Current_Route[2])
            Fare += F
            continue
    
    else:
        print("Seat Occupied")
        print("Choose A Different Seat")

  elif Option1 == 5:
    print("\nConfirm Tickets: ")
    print(f'Passengers: {Passengers}')
    print(f'Seats: {Seates}')
    print(f'Cost: {Fare}')
    C = input("\nBook Tickets (y/n): ")
    
    if C == 'y':
      print("\nTickets Booked Successfully !!")
      print("Enjoy Your Ride")
      break

    elif C == 'n':
      print("\nTickets Cancelled")
      break
  elif Option1 == 6:
    print("\nTickets Cancelled")
    break

  else:
    print("\nInvalid Option")
    continue