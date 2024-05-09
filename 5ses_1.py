# Juceklis

# Lietotājs ievada vārdu.

# Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?

# Valdis -> Sidlav, pamatigs juceklis vai ne V

user_name = input("Please write name ")
reverse_name = user_name[::-1]
upper_name = reverse_name[0].upper()
lower_name = reverse_name[-1].lower()
name = upper_name + reverse_name[1:-1] + lower_name
pname = user_name + " -> " + name + ", pamatigs juceklis vai ne " + user_name[0]
print(pname)