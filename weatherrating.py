temp = float(input("What is the temperature?"))

if temp > 0 and temp <=15:
    print("Cold")
elif temp > 15 and temp <20:
    print("Chilly")
elif temp >= 20 and temp <30:
    print("Perfect")
elif temp >= 30 and temp <40:
    print("Hot")
elif temp >=40 and temp <50:
    print(Hot)
elif temp > 50 or temp <0:
    print("Oh shiet")
else:
    print(f"{temp} is not an available temperature")