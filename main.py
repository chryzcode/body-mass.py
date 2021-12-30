# collecting data from users(float[decimal])
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# getting the bmi 
bmi = weight / (height/100)**2
# printing out the BMI using the format function 
print(f'Your BMI is {bmi}')

# conditional statement in dictating feedback 
if BMI < 18.5:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
else:
    print("You are obese.")
