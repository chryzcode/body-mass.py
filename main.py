# collecting data from users(float[decimal])
try:
    height = float(input("Enter your height in cm: "))
except ValueError:
    print("You have entered an invalid value")
    quit()

try:
    weight = float(input("Enter your weight in kg: "))
except ValueError:
    print("You have entered an invalid value")
    quit()

# getting the bmi 
bmi = weight / (height/100)**2
# printing out the BMI using the format function 
print(f'Your BMI is {bmi}')

# conditional statement in dictating feedback 
if bmi < 18.5:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are over weight.")
else:
    print("You are obese.")
