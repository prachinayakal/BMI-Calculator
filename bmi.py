def bmi_calculator():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi}")

bmi_calculator()
