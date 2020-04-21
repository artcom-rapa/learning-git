
masa_roquefort = 2
cena_roquefort = 12.50
roquefort = "Roquefort, %.2f kg, %.2f zł" % (masa_roquefort, cena_roquefort)

masa_stilton = 1
cena_stilton = 11.24
stilton = "Stilton, %.2f kg, %.2f zł" % (masa_stilton, cena_stilton)

masa_brie = 1
cena_brie = 9.30
brie = "Brie, %.2f kg, %.2f zł" % (masa_brie, cena_brie)

masa_gouda = 1
cena_gouda = 8.55
gouda = "Gouda, %.2f kg, %.2f zł" % (masa_brie, cena_brie)

masa_edam = 1
cena_edam = 11.00
edam = "Edam, %.2f kg, %.2f zł" % (masa_edam, cena_edam)

masa_parmezan = 3.5
cena_parmezan  = 16.50
parmezan = "Parmezan, %.2f kg, %.2f zł" % (masa_parmezan, cena_parmezan)

masa_mozzarella = 0.130
cena_mozzarella = 14.00
mozzarella = "Mozzarella, %.2f kg, %.2f zł" % (masa_mozzarella, cena_mozzarella)

masa_hit = 0.22
cena_hit = 122.32
hit = "Hit, %.2f kg, %.2f zł" % (masa_hit, cena_hit)

masa_listek_mietowy = 0.2
cena_listek_mietowy = 20.00
listek_mietowy = "Listek mietowy, %.2f kg, %.2f zł" % (masa_listek_mietowy, cena_listek_mietowy)

suma = cena_roquefort + cena_stilton + cena_brie + cena_gouda + cena_edam + cena_parmezan + cena_mozzarella + cena_hit + cena_listek_mietowy
suma_calkowita = "Suma zł: %.2f" % (suma)

raport = "Raport z zakupów:\n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s" % (roquefort, stilton, brie, gouda, edam, parmezan, mozzarella, hit, listek_mietowy, suma_calkowita )

print(raport)

print("'Hiszpańska inkwizycja' to nalepszy skecz grupy Monty Pythona")
