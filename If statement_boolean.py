

vehicle_type = "Truck"

if vehicle_type.upper().startswith("P"):
    print(vehicle_type, 'starts with "P"')
else:
    print(vehicle_type, 'does not start with "P"')


year = "2001"

if year.isdigit():
    print(year, "is all digits")
else:
   pass


hot_plate = True

if hot_plate:
    print("Be careful, hot plate!")
else:
    print("The plate is ready.")
