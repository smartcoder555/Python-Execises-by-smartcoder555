#Height-converter

Height=float(input("Type your Height to convert:"))
Unit=str(input(f"Is it Inches or CentiMetres (in/cm):"))

if Unit== "cm" :
    Height=Height / 2.54 
    Unit= "in"

elif Unit== "in":
    Height= Height * 2.54
    Unit= "cm"
else:
    print("Your Unit is incorrect please refresh and type between these two units(in/cm)")

print(f"Your height is {round(Height,4)}{Unit}")