speed = float(input("Enter your speed: "))
unit = input("m/s or km/h? ")
if unit == "m/s":
    answer = speed*3.6
    print(answer,"km/h")
elif unit == "km/h":
    answer = speed/3.6
    print(answer,"m/s")
else:
    print(f"{unit} is not availble")