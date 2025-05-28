from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
#************************
"""
verification si la chaine contient seulement des lettres miniscules
"""
def LettresMiniscule(ch):
    ok=True
    """on suppose toujours au départ que la condition est verifier (ok=true),
       on incremente (i=i+1) jusqu'à on trouve l'opposé(ok=False) on bien on arrive à la fin de la chaine
    """
    i=0
    while(i<= len(ch)-1 and ok ==True):
        if not(ord('a') <= ord(ch[i]) <= ord('z')) and ch[i] != " " :
            ok=False
        else:
            i=i+1
    return ok
#************************
def UnSeulEspace(ch):
    ok= True
    
    """on suppose toujours au départ que la condition est verifier (ok=true),
       on incremente (i=i+1) jusqu'à on trouve l'opposé(ok=False) on bien on arrive à la fin de la chaine
    """
    i=0
    
    while(i<= len(ch)-2 and ok == True):
        if(ch[i]==" " and ch[i+1]==" "):
             ok=False
        else:
            i=i+1
    return ok
def crypterMot(mot):
    nvmot=""
    for i in range(len(mot)-1,-1,-1):
        nvmot=nvmot+mot[i]
    return nvmot
"""
****une autre solution:
def Miroir(ch):
    ch1=""
    for i in range(len(ch)):
        ch1=ch[i]+ch1
    return ch1

"""
def miroir(ph):
    phcryptée=""
    i=0
    pos=0
    """
    while(len(ph) !=0 and lastword !=True):
        if(ph.find(" ") ==-1 ) :
            lastword=True
            """
    while(pos !=-1):
            
        pos=ph.find(" ")
        if(pos==-1):
            mot=ph
        else:    
           mot=ph[:pos]
           ph=ph[pos+1:]
        
        #*******construction de la chaine cryptée**********
        if(phcryptée==""):
          phcryptée=crypterMot(mot)
        else:
          phcryptée=phcryptée+" "+crypterMot(mot)
        
    return phcryptée
        
    
    
    
#*************************
def Play():
    """ *******recuperation de la chaine***************************
    """
    ch=w.ch.text()
    """
      *********Controle de saisie**********************************
    """
    
    if( ch== ""  or len(ch)<50 or LettresMiniscule(ch)== False):
        print(len(ch))
        msg= "Veuillez introduire une chaîne"
    else:
        
       if(UnSeulEspace(ch)== False):
           msg="Entre 2 mots un seul espace est autorisé"
       else:
           """
               ********************* traitement miroire ****************************
           """
           msg=miroir(ch)
           
    w.msg.setText(msg)           
            
        
    
    










#**************************
app=QApplication([])
w=loadUi("InterfaceMiroirsMots.ui")
w.show()
w.Miroir.clicked.connect(Play)
app.exec_()


