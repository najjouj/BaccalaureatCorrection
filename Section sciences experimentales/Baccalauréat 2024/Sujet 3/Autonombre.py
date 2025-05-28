from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
#*****************************
def SommeChiffres(X):
    S=0
    while(X != 0):
        S = S + X % 10
        X = X // 10
    return S
#*****************************
def Verifier(X):
   
    ok= True
    i=10
    while(i<= X and ok == True):
        
        if(X == SommeChiffres(i)+i):
            ok = False
        else :
            i=i+1
    return ok        
        
        
#*****************************
def Chercher(N,M):
    i=N
    msg=""
    while( i <= M):
        if(Verifier(i) == True):
            if(msg==""):
                msg=str(i)
            else:    
                msg =msg+" - "+str(i)
        i=i+1
    return msg    
    
    
#***************************** 
def Play():
    N=int(w.N.text())
    M=int(w.M.text())
    if(Verifier(97)==True):
       print("yyyyyy")
    if(N <20 or N > 50 or M < N or M > 100):
        w.msg.setText("Veuillez respecter : 20 <= N et N<M<=100")
    else:
        if( Chercher(N,M) == ""):
              w.msg.setText("Aucun Autonombre entre "+str(N)+" et "+str(M))
        else:
              w.msg.setText("Le(s) nombre(s) Autonombre(s) : "+ Chercher(N,M))
                  
#*****************************    
app=QApplication([])
w=loadUi("InterfaceAutonombre.ui")
w.show()
w.Afficher.clicked.connect(Play)
app.exec_()