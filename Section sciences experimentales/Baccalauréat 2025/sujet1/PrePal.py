from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem

def Palindrome(CH):
    i=0
    j=len(CH)-1
    while(i<j) and (CH[i]==CH[j]):
        i=i+1
        j=j-1
    return i >= j
def Premier(N):
    i=2
    test=True
    while (test != False and i < N):
        if(N % i ==0):
            test =False
        else :
            i=i+1
    return test
def Verif(CH):
    return Premier(int(CH)) and Palindrome(CH)

def play():
    N=w.N.text()
    if(len(N)<3 or not (N.isdecimal())):
        w.msg.setText("N doit être de 3 chiffres au minimun")
    else :
        if not Verif(N):
            w.msg.setText(N+" n'est pas premier palindrome")
        else:
            w.msg.setText(N+" est premier palindrome")
        
        
        
        

app = QApplication([])
w = loadUi ("Interface.ui")
w.show()
w.verifier.clicked.connect (play)
app.exec_()