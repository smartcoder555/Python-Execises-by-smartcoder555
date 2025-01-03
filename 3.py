#Calculating base
import math

print("To get Base")

z1=float(input("Enter your number to be Hypotenuse:"))
z2=float(input("Enter your number to be Perpendicular:"))

B= math.sqrt((pow(z1,2) - pow(z2,2)))

print(f"Your Base is = {B}")