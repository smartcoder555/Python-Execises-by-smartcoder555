#Shopping Cart Program

Items= []
Prices= []
Total = 0


while True:
     Item= str(input("Please Enter your item you want to buy (Type e to exit shopping mode) :"))
     if Item.lower()=="e":
        break
     else:
        Price=float(input("Please Enter the Price of your Item you want to buy :"))
        Items.append(Item)
        Prices.append(Price)

print("Your Cart")

for Item in Items:
    print(f"{Item}")

for Price in Prices:
    Total=Total + Price   

print(f"Your total is = ₹{Total:,.2f}")