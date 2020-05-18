from math import *
from random import *
from time import *


# print(x, end=" ") par défaut après un print on a une \t, qui se change avec end = ...

###############
## FONCTIONS ##
###############

def Infosperso(prenom, nom, age, sexe):
    prenom = str(input("Prenom : "))
    temp_prenom = prenom[0]
    prenom = temp_prenom.upper() + prenom[1:]
    nom = str(input("Nom : ").upper())
    age = int(input("Age : "))
    sexe = str(input("H/F : "))
    sexe = sexe[0]
    print(sexe)
    if(sexe == 'h' or sexe == 'H' or sexe == 'f' or sexe == 'F'):
        val = 1
    else:
        val = 0
    while val == 0:
        print("ERREUR de saisie")
        sexe = str(input("\tMerci de resaisir H/F : "))
        sexe = sexe[0]
        if(sexe == 'h' or sexe == 'H' or sexe == 'f' or sexe == 'F'):
            val = 1
        else:
            val = 0
    if ((sexe == 'h') or (sexe == 'H')) and (age >= 18):
        print("Bonjour M.",prenom, nom, "\b.")
    elif ((sexe == 'h') or (sexe == 'H')) and (age < 18):
        print("Salut, cher",prenom, nom, "\b.")
    elif ((sexe == 'f') or (sexe == 'F')) and (age >= 18):
        print("Bonjour Mme.",prenom, nom, "\b.")
    else:
        print("Salut, chère",prenom, nom, "\b.")
    return prenom, nom, age, sexe

def Decompte():
    global dec
    i = dec
    i = int(input("Valeur début decompte : "))
    while i > 0:
        print(i)
        i = i-1
    print("BOOUUUUMMM")

def Concat():
    i = "O"
    concat = str(input("val : "))
    while (i=="O"):
        temp = str(input("val : "))
        concat = concat + temp
        i = str(input("autre valeur (O/N) : "))
        i = i[0].upper()
        print(i)
    return concat

def Repetition():
    val = str(input("Valeur à dupliquer : "))
    nb = int(input("nb de repetitions : "))
    val = val * nb
    return val

def RandomInt():
    min, max = int(input("min : ")), int(input("max : "))
    aleat = int(randint(min,max))
    if aleat>((min+max)/2):
        print("aleat > ", (min+max)/2, "\naleat = ", aleat)
    elif aleat<(max/2):
        print("aleat < ", (min+max)/2, "\naleat = ", aleat)
    else:
        print("aleat = ", (min+max)/2)

def Superficie():
    largeur = int(input("largeur (en m) : "))
    longueur = int(input("longueur (en m) : "))
    superficie = largeur * longueur
    print("La superficie du terrain est de ", superficie, "m2.\nCela correspond à ", superficie/10e3, "hectares.")

def Secondes():
    heure = str(input("Saisir l'heure au format hh:mm:ss : "))
    hh = heure[0:2]
    mm = heure[3:5]
    ss = heure[6:8]
    hh = int(hh); mm= int(mm); ss = int(ss)
    while(mm>60):
        mm = int(input("resaisir les minutes (<60) : "))
        while(ss>60):
            ss = int(input("resaisir les secondes (<60) : "))
    mm = mm * 60
    hh = hh * 3600
    secondes = mm + hh + ss
    print("L'heure saisie correspond à", secondes, "secondes.")

def TVA():
    prix = int(input("Prix HT : "))
    nb = int(input("Nb d'articles : "))
    tva = int(input("Taux de TVA (en %) : "))
    prixTTC = prix * nb 
    prixTTC += (tva/100)*prixTTC
    print("Le prix TTC pour cet achat est de :", prixTTC)

def Heure():
    temps = int(input("Saisir temps en secondes : "))
    if temps <60:
        ss = temps
    else:
        hh = float(temps / 3600)
        mm = float((hh - int(hh)) * 60)
        ss = float((mm - round(mm)) * 60)
    print(int(hh), ":", round(mm), ":", round(ss))

def KMtoMiles():
    dist = float(input("Distance en km : "))
    tmp = dist
    dist /= 1.609
    print(tmp,'kms =', round(dist,2),"miles.")

def Liste():
    liste = list()
    c ='O'
    while (c == "O"):
        liste.append(str(input("val : ")))
        c = str(input("autre valeur ? (O/N) : "))
        c = c.upper()
    return liste

def BoucleForInfos(liste):
    print("Vos informations :")
    for i in liste:
        print(i)

def BoucleForRange(a, b):
    for i in range(a, b):
        print(i*b - a)

def BoucleListe(liste):
    a = 1
    for i in liste:
        print("element", a, ":", i)
        a += 1


###############
#### PRGRM ####
###############
prenom, nom, age, sexe, dec = str(), str(), int(), str(), int()
infos = Infosperso(prenom, nom, age, sexe)
prenom = infos[0]; nom = infos[1]; age=infos[2]; sexe=infos[3]
Decompte()
concat = Concat()
print(concat)
valdupliquee = Repetition()
print(valdupliquee)
RandomInt()
Superficie()
Secondes()
TVA()
Heure()
KMtoMiles()
BoucleForInfos(infos)
a, b = int(input("Valeur min. range : ")), int(input("Valeur max. range : "))
BoucleForRange(a, b)
liste = Liste()
print(liste)
BoucleListe(liste)