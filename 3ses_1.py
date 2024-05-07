# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.

# Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
# Ja ir pāri 37, tad izvadiet "iespējams drudzis"

temp = float(input("Your temperature? "))
low = float(35)
max = float(37)

if (temp < low):
    print("Nav par aukstu?")
elif temp > max:
    print("Iespējams drudzis")
else :
    print("Viss kārtībā")