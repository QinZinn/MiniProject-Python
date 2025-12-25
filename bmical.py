name = input("Enter your name: ")
h = int(input("Enter your height (cm): "))
m = float(input("Enter your weight (kg): "))
def bmi(weight, height):
    return weight / ((height/100)**2)
print("Your bmi is: ",round(bmi(m,h),2))