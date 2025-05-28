from numpy import array

tab= array([float()]*10)

for i in range(10):
    tab[i]=float(input("donner un nombre:"))
    
max=tab[0]
p=0
for i in range(10):
    if tab[i]>max:
        max=tab[i]
        p=i
        
print("la valeur maximale est:",max,"  la position est:",p)        