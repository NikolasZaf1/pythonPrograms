# -*- coding: utf-8 -*-
"""ΑΣΚΗΣΗ_ΚΩΔΙΚΑ_ΕΝΟΤΗΤΑΣ_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10iNuimtC-5hL4zcqSJyMjMnIIcgeP5pV
"""

import math
#code for enotita_1
print("THE BASIC HYPOTHESIS: USER INPUT ALWAYS IS VALID AND NO CHECK WITH TRY EXCEPT ERROR")
print()
print("Enter the a1 parameter:")
a1 = int(input())


print()
print("Enter the a2 parameter:")
a2 = int(input())


print()
print("Enter the b1 parameter:")
b1 = int(input())


print()
print("Enter the b2 parameter:")
b2 = int(input())


#compute ΑΡΙΘΜΗΤΗΣ
a_b =(a1*b1)+(a2*b2)

#compute ΠΑΡΑΝΟΜΑΣΤΗΣ
a = abs(math.sqrt(a1**2+a2**2))
b = abs(math.sqrt(b1**2+b2**2))

#computing cos
costh = a_b / (abs(a)*abs(b))

#computing degree

# Calculate theta with arccos in radians!
theta = math.acos(costh)
print('Theta in radians: {}'.format(round(theta, 4)))
# Convert to degrees!
goniath = math.degrees(theta)
print('Theta in degrees: {}'.format(round(goniath, 4)))


print()

print("the cosine is")
print(costh)
print("the angles in degrees of cosine is")
print(goniath)