import joblib

import numpy as np

classifier=joblib.load('medi-insurance.pkl')

age = int(input("Enter the age: "))
children = int(input("Enter the number of children: "))
sex = float(input("Enter the sex: "))
region = input("Enter the region: ").lower() == "yes"
charges = float(input("Enter the charges: "))
bmi = float(input("Enter the BMI (Body Mass Index): "))
smoker = input("Enter the smoker (yes/no): ").lower() == "yes"



# changing input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = regressor.predict(input_data_reshaped)
print(prediction)

print('The insurance cost is USD ', prediction[0])

if (prediction[0] == 0):
  print('The person has no insurance')
else:
  print('The person has no insurance')