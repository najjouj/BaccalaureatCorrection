def SaisirNombreEleves():
    NBE=int(input("Entrer le nombre des élèves :"))
    while not( NBE >= 0 and NBE <=40):
        NBE=int(input("Entrer le nombre des élèves :"))
    return NBE    

def SaisirNotes(Notes,NBE):
    
    for i in range(NBE):
      Notes[i]=float(input("Donner la moyenne n°"+str(i+1)+": "))
      while not(Notes[i] >=0 and Notes[i] <= 20):
          Notes[i]=float(input("Donner la moyenne n°"+str(i+1)+": "))
def AffichageNotes(Notes,NBE):
    for i in range(NBE):
        print("Moyenne n° "+str(i+1)+" "+str(Notes[i]))
        
def MaxNotes(Notes,NBE):
    mx=Notes[0]
    for i in range(1,NBE):
        if(mx < Notes[i]):
            mx=Notes[i]
    return mx
def MinNotes(Notes, NBE):
    mn=Notes[0]
    for i in range(1,NBE):
        if(mn> Notes[i]):
            mn=Notes[i]
    return mn
def MoyenneNotes(Notes, NBE):
    s=0
    for i in range(NBE):
        s=s+Notes[i]
        
    return (s/NBE)

from numpy import array
NBE=SaisirNombreEleves()

Notes= array([float()] * NBE)
SaisirNotes(Notes, NBE)
AffichageNotes(Notes, NBE)
print("La moyenne maximale de la classe est:"+str(MaxNotes(Notes,NBE)))
print("La moyenne minimale de la classe est:"+str(MinNotes(Notes,NBE)))
print("La moyenne de la classe est:"+str(MoyenneNotes(Notes,NBE)/NBE))
  
    