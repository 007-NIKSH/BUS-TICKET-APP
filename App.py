Route_1 = ['Bangalore', 'Hyderabad', '1798']
Route_2 = ['Chennai', 'Bangalore', '1448']
Route_3 = ['Chennai', 'Kochi', '2728']
Route_4 = ['Pune', 'Mumbai', '653']
Route_5 = ['Mumbai', 'Delhi', '3259']
Passengers = []
Age = []
Fare = 0

Tru1 = False
Try2 = False

def Routes_Print():
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

print(Routes_Print())
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
  print("3 - Add Passenger")
  print("4 - Book Tickets")
  print("5 - Exit")
  Option1 = int(input("\nOption: "))

  if Option1 == 1:
    print(f'\nPassengers: {Passengers}')
    continue

  elif Option1 == 2:
    print(f'\nCost: {Fare}')

  elif Option1 == 3:
    print("\nPassengers Details: ")
    A = input("Name: ")
    B = int(input("Age: "))
    Passengers.append(A)
    Age.append(B)

    if B <= 10:
      Fare += 0
      continue

    else:
      F = int(Current_Route[2])
      Fare += F
      continue

  elif Option1 == 4:
    print("\nConfirm Tickets: ")
    print(f'Passengers: {Passengers}')
    print(f'Cost: {Fare}')
    C = input("\nBook Tickets (y/n): ")
    
    if C == 'y':
      print("\nTickets Booked Successfully !!")
      print("Enjoy Your Ride")
      break

    elif C == 'n':
      print("\nTickets Cancelled")
      break
  elif Option1 == 5:
    print("\nTickets Cancelled")
    break

  else:
    print("\nInvalid Option")
    continue