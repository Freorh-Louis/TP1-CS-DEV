# Programme testant la valité d'une date

import TP1_fonction

# main de l'exo 2
print('date est un string à rentrée au format "jj/mm/aaaa"')
date = input("date = ")

if TP1_fonction.date_valide(date):
    print("date valide")
else:
    print("date non valide")


# main de l'exo 3
print("entrer votre revenu sous forme de float positif")
revenu = int(input("revenu = "))
print(TP1_fonction.mesImpots(revenu))


# main de l'exo 6
for i in range(1,1001):
    altitude_max = 0
    temps_de_vol_max = 0
    altitude_i = TP1_fonction.altitude_max(TP1_fonction.syracuse(i))
    temps_de_vol_i = TP1_fonction.temps_de_vole(TP1_fonction.syracuse(i))
    if altitude_i > altitude_max:
        altitude_max = altitude_i
    if temps_de_vol_i > temps_de_vol_max:
        temps_de_vol_max = temps_de_vol_i

print(altitude_max,temps_de_vol_max)


