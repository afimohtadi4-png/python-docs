from numpy import array
def saisir():
    N=int(input("n="))
    while N<=0 :
        N=int(input("n="))
    return N
def remplir(N,T):
    for i in range(N):
        T[i]=int(input("donner T["+str(i)+"]="))
def somme(N,T):
    s=0
    for i in range (N):
        s=s+T[i]
    return s
#pp
N1=saisir()
N2=saisir()
T1=array([int()]*20)
T2=array([int()]*20)
remplir(N1,T1)
remplir(N2,T2)
print("la somme du premier tableau est ="+str(somme(N1,T1)))
print("la somme du deuxieme tableau est ="+str(somme(N2,T2)))
