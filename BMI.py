weight = input('Enter your weight in kg ')
height = input('Enter your height in cm ')
weight = float(weight)
height = float(height)
height = height / 100
bmi = weight / (height ** 2)
print( 'Your BMI is', bmi)

if bmi < 18.5:
    print('You are underweight!')
elif bmi >= 18.5 and bmi <24:
    print('Your weight is normal!')
elif bmi >= 24 and bmi < 27:
    print('You are overweight!')
elif bmi >= 27 and bmi < 30:
    print('You are mildly obese!')
elif bmi >= 30 and bmi < 35:
    print('You are moderately obese!')
else:
    print('You are severely obese!')    






