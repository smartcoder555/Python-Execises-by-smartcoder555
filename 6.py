#Compound Interest Calculator

P= 0
R=0
T=0

while   P<=0 :
    P= float(input("Type your Principal Amount:"))
    if P<=0 :
     print("Your Principal Amount Can't be Negative and = 0 Please type it in positive value or can't be leaved;")

while R<=0 :
    R=float(input("Type your Rate of Interest:"))
    if R<=0 :
     print("Your Rate of interest Can't be Negative and = 0 Please type it in positive value;")


while T<=0 :
    T=float(int(input("Type your Time(in years):")))
    if T<=0:
     print("Your Time Can't be Negative and = 0 Please type it in positive value;")


print("Your Data checker")


print(f"P = {P}")
print(f"R = {R}")
print(f"T = {T}")
CI= P * pow(1+R/100,T)

print(f"Your Compound Interest is = ₹{CI} ")