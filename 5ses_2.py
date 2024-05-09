# Uzrakstīt programmu teksta simbola atpazīšanai

# Lietotājs(pirmais spēlētājs) ievada tekstu.

# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt

# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 

# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.

# Kartupeļu lauks -> ********* *****

# ievada a -> *a****** *a***

# Principā tas ir labs iesākums karātavu spēlei.

name = input("First player enters text ")

def display(name):
    display_name = ""
    for letter in name:
        if letter in name_symbol:
            display_name +=letter
        else:
            display_name += "~"
    return display_name

print(display)
    
name_symbol = input("Second player enters symbol ")

