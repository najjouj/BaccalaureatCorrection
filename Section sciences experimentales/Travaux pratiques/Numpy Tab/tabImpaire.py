from numpy import array

# taille du tableau fixe (10)


"""
tab=array([int()]*10)

for i in range (10) :
    tab[i]=int(input("Donner un nombre:"))
               
for i in range (10):
               if (tab[i] % 2) != 0:
                 print(tab[i])
"""

# taille du tableau donner par l'utilistateur
"""
nb=int(input("donner le nombre des valeurs à saisir:"))

tab= array([int()]* nb)
for i in range (nb) :
    tab[i]=int(input("Donner un nombre:"))
               
for i in range (nb):
               if (tab[i] % 2) != 0:
                 print(tab[i])
                 """
# deux tableaux paires & impaires
nb=int(input("donner le nombre des valeurs à saisir:"))

tab= array([int()]* nb)
paires= array([int()]* nb)
impaires= array([int()]* nb)
for i in range (nb) :
    tab[i]=int(input("Donner un nombre:"))
j=0
k=0               
for i in range (nb):
              
               if (tab[i] % 2) != 0:
                 impaires[j]=tab[i]
                 j=j+1
               else:
                     paires[k]=tab[i]
                     k=k+1
print(k)
print(j)
                     
for i in range(j):
    
    print(impaires[i])
for i in range(k):
    
    print(paires[i])
                     
