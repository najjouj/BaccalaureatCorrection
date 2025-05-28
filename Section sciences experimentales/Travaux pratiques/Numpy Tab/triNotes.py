from numpy import array

notes=array([float()] *10)

# remplissage du tableau
def Remplir(notes):
    for i in range(5):
      notes[i]=float(input("donner une note:"))

        
        
      
# Affichage du tableau des moyennes
def Affichage(notes):
    print("la liste des moyennes est:")
    for i in range(5):
        print(notes[i])
  
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
# tri **** permuter les moyennes
def permuter(notes,i):
    v=notes[i]
    notes[i]=notes[i-1]
    notes[i-1]=v
#tri ***** reorganisation des moyennes
def reorganiser(notes,i):
    
    if(notes[i-1]>notes[i]) and (i-1 >=0):
      permuter(notes,i)
      reorganiser(notes,i-1)   
    
# tri des moyennes des élèves
def TriMoy(notes):
    for i in range(5):
        if(notes[i]<notes[i-1]):
           reorganiser(notes,i)
#*****************test**********************
def test():
    print("hello")
# programme principal
Remplir(notes)
Affichage(notes)
print("La moyenne de la classe est:",Moyenne(notes))
print("La moyenne maximle de la classe est:",MoyMax(notes))
print("La moyenne minimale de la classe est:",MoyMin(notes))
TriMoy(notes)
print("*********** Après Tri *************************")
Affichage(notes)
