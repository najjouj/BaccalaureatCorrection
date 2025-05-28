
from numpy import array

notes=array([float()] *10)
print("rtest")

for i in range(5):
  notes[i]=float(input("donner une note:"))
  
moy=0
for i in range(5):
   moy=moy+notes[i]
   
print("la moyenne de la classe est :",moy/5)
  
            