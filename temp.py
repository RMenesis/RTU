temp = float(input("Your temperature? "))
low = float(35)
max = float(37)

if (temp < low):
    print("Nav par aukstu?")
elif temp > max:
    print("Iespējams drudzis")
else :
    print("Viss kārtībā")