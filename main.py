


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



suma = cena_edam + cena_parmezan + cena_mozzarella + cena_hit
suma_calkowita = "Suma zł: %.2f" % (suma)

raport = "Raport z zakupów:\n %s \n %s \n %s \n %s \n %s " % (edam, parmezan, mozzarella, hit, suma_calkowita )

print(raport)



