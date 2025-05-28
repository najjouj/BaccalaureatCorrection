from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

#*****************************************************************
def Trier(CH):
    PERMUT = True
    while PERMUT :
        PERMUT = False
       
        for k in range(0,len(CH)-2,2):
            
            BLOC1= CH[k:k+2]
            BLOC2= CH[k+2:k+4]
            if BLOC1 > BLOC2 :
                CH = CH[0:k]+BLOC2+BLOC1+CH[k+4:len(CH)]
                PERMUT = True
    return CH

#*******************************************************************
def verifSuite(CH):
    r=int(CH[2:4])-int(CH[0:2])
    i=2
    while r != 0 and i<= len(CH)-4:       
       if(r != int(CH[i+2:i+4])-int(CH[i:i+2])):
            r=0
             
       i=i+2
      
    return r    
        
#*******************************************************************

def Play():
   X=w.X.text()
   if(len(X) % 2!=0 or len(X)<6 or len(X)>20):
       w.msg1.setText("Veuillez saisir un nombre de 6 à 20 chiffres et de longueur paire")
   else:    
     X=Trier(X)
     w.msg1.setText("Les tranches de chiffres triées "+X)
     if(verifSuite(X)!=0):
        w.msg2.setText("forment des termes d'une suite arithmétiques(r="+str(verifSuite(X))+")")
     else:
        
        w.msg2.setText("ne forment pas des termes d'une suite arithmétique")
    









app=QApplication([])
w=loadUi("InterfaceArithmétique.ui")
w.show()
w.verifier.clicked.connect(Play)
app.exec_()