from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem

def PGCD(A,B):
    while B != 0:
        R = A % B
        A = B
        B = R
    return A    
def Verif(N,B):
    return (N % B ==0) and (PGCD(B,N //B)==1)
def Unitaire(N):
    i=2
    msg=""
    while(i <10 ):
        if(Verif(N,i)):
            if msg=="":
                msg=str(i)
            else:
                 msg=msg+", "+str(i)
        i =i+1        
            
    return msg        

def play():
    #<print(Unitaire(901))
    N=w.N.text()
    if(len(N)!=3 or not (N.isdecimal())):
        w.msg.setText("N doit être de 3 chiffres!")
    else:
        if(Unitaire(int(N))==""):
          w.msg.setText(N+" ne possede aucun diviseurs!")
        else :
            w.msg.setText("Les diviseurs de "+N+" sont: "+Unitaire(int(N)))
    

app = QApplication([])
w = loadUi ("Interface.ui")
w.show()
w.Afficher.clicked.connect (play)
app.exec_()