
from numpy import array

notes=array([float()] *5)

# remplissage du tableau
def Remplir(notes):
    for i in range(5):
      notes[i]=float(input("donner une note:"))
  
# calcul de la moyenne de classe  
    
def Moyenne(notes):
    moy=0
    for i in range(5):
      moy=moy+notes[i]
   
    return moy/5

# calcul de la moyenne maximale

def MoyMax(notes):
    max=notes[0]
    for i in range(5):
        if(max<notes[i]):
            max=notes[i]
    return max
# calcul de la moyenne minimale
def MoyMin(notes):
    min=notes[0]
    for i in range(5):
        if(min>notes[i]):
            min=notes[i]
    return min
# programme principal
Remplir(notes)
print("La moyenne de la classe est:",Moyenne(notes))
print("La moyenne maximle de la classe est:",MoyMax(notes))
print("La moyenne minimale de la classe est:",MoyMin(notes))
    
  
            