from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Horner(Z):
    M=0
    while( Z != ""):
        CH=Z[0]
        M=(M * 2 +int(CH)) % 7
        Z=Z[1:len(Z)]
    return M
#***********************************************
def Etape2(Y):
    Z=""
    i=0
    if(len(Y) % 2 !=0):
        Z=Z+ str(int(Y[0]) % 7)
        i=1
    
    while(i<len(Y)):
            Z=Z+str(int(Y[i:i+2]) % 7)
            i=i+2
    return Z        
        
def Etape1(X):
    Y=""
    for i in range(len(X)):
        Y=Y+str(int(X[i]) % 7)
    return Y    




def Play():
    X=w.X.text()
    if(len(X)<5 or len(X)>20):
        w.msg.setText("Veuillez saisir un nombre de 5 à 20 chiffres")
    else:    
     Y=Etape1(X)
     Z=Etape2(Y)
     if(Horner(Z) == 0):
        msg= str(X)+ " est divisible par 7"
     else:
        msg= str(X)+ " n'est pas divisible par 7"
        
     w.msg.setText(msg)       
    
    







app=QApplication([])
w=loadUi("InterfaceHorner.ui")
w.show()
w.Verif.clicked.connect(Play)
app.exec_()
