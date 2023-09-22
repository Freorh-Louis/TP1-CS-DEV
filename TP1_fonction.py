# Fonctions associées au TP1    22/09/2023   Louis VINCENT

# Fonction testant si l'année est bissextile
# année est un int
def bissextile(annee):
    if annee%4 == 0 and annee%100 != 0:
        return(True)
    elif annee%400 == 0:
        return(True)
    else:
        return(False)


# Fonction renvoyant le nombre de jours dans un mois d'une année donné
# mois est un int entre 1 et 12 et année est un int
def nbr_jours(mois,annee):
    jours = 0
    if mois == 2:
        if bissextile(annee):
            jours = 29
        else:
            jours = 28
    elif mois in [4,6,9,11]:
        jours = 30
    else:
        jours = 31
    return(jours)


# Fonction qui vérifie la validité d'une date
# date est un string au format "jj/mm/aaaa"
def date_valide(date):
    jour,mois,annee = date.split("/")
    jour_valide,mois_valide = False,False
    if int(jour) > 0 and int(jour) <= nbr_jours(int(mois),int(annee)):
        jour_valide = True
    if int(mois) > 0 and int(mois) <= 12:
        mois_valide = True
    return(jour_valide and mois_valide)


# Calcul des impots pour un revenu donner
# revenu est un float positif
def mesImpots(revenu,impot = 0):
    if revenu <= 10225:
        return(impot)
    elif revenu >= 160336:
        impot += (revenu-160336)*0.45
        return mesImpots(160335,impot)
    elif revenu >= 75546:
        impot += (revenu-75546)*0.41
        return mesImpots(75545,impot)
    elif revenu >= 26071:
        impot += (revenu-26071)*0.3
        return mesImpots(26070,impot)
    elif revenu >= 10226:
        impot += (revenu-10226)*0.11
        return mesImpots(10225,impot)


# vérifie si 2 nombre a et b sont amicaux
# a et b sont des nombres entiers postifs
def nombre_amicaux(a,b):
    somme1 = 0
    somme2 = 0
    for i in range(1,max(a,b)+1):
        if a%i == 0:
            somme1 += i
        if b%i == 0:
            somme2 += i
    return(a+b == somme1 == somme2)


# Crée une liste avec les valeurs de la suite de syracuse de N
# N est un entier postif
def syracuse(N):
    syracuse = [N]
    while N != 1:
        if N%2 == 0:
            N = int(N/2)
        else:
            N = int(N*3 + 1)
        syracuse.append(N)
    return(syracuse)


# Calcul l'altitude maximal atteinte lors d'une suite de syracuse
# syracuse est une suite
def altitude_max(syracuse):
    altitude_max = syracuse[0]
    for e in syracuse:
        if e > altitude_max:
            altitude_max = e
    return(altitude_max)


# Calcul le temps de vole d'une suite de syracuse
# syracuse est une liste
def temps_de_vole(syracuse):
    return(len(syracuse))


def Hanoi(n,o,d):
    m = 6-o-d
    if n == 1:
        print(o,"vers",d)
    else:
        Hanoi(n-1,o,m)
        Hanoi(1,o,d)
        Hanoi(n-1,m,d)

Hanoi(3,1,3)