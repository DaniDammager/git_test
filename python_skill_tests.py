#import numpy as np 

name = "Daniel"
surname = "Berreth"
age = 28
print("My name is %s %s and I am %d years old." %(name, surname, age)) 

if age < 30:
    print("%s %s is younger than 30 years old." %(name, surname))

count = 0
while count < 3: 
    print ("It is Loop No.%d atm." %count)
    count += 1

for x in range(0, int(age/10)):
    print("%s %s already had his round birthday No.%d." %(name, surname, x+1))

#height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
#weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

#np_height = np.array(height)
#np_weight = np.array(weight)
#bmi_list = np_weight / np_height**2
#print(bmi_list)