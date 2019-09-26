from matplotlib import pyplot as pl
from math import sqrt as s
from math import pi
from math import asin
from math import acos
from math import sin
from math import cos
from math import pow
from math import hypot
from math import sqrt as root2

x=int(input("Re(z): "))
y=int(input("Im(z): "))
n=int(input("Indice della radice: "))
risoluzione=0.001
if y>=0:
    print("z=",x,"+i",y)
else:
    y*=-1
    print("z=",x,"-i",y)
    y*=-1

p=hypot(x,y)
teta1=acos(float(x/p))
teta2=asin(float(y/p))

if teta1-teta2>=0.01:
    print("Errore: i valori di teta sono diversi")

assex=[]
assey=[]
ro=pow(p,float(1/n))
theta=float(teta1/n)

for k in range(0,n):
    duekpi=float(2*k*pi/n)
    arg_e_pi=theta+duekpi
    tmpx=(cos(arg_e_pi))
    tmpy=(sin(arg_e_pi))
    assex[k:k]=[tmpx*ro]
    assey[k:k]=[tmpy*ro]

x=[]
y1=[]
y2=[]
w=ro*(-1)
n=0
while w<=ro:
    x[n:n]=[w]
    y1[n:n]=[root2(x[0]**2-x[n]**2)]
    y2[n:n]=[(-1)*y1[n]]
    w+=risoluzione
    n+=1

w=w-float(w/5)
ro=ro+float(ro/5)
riga=[]
zero=[]
i=0
w=(-1)*ro
while w<=ro:
    riga[i:i]=[w]
    zero[i:i]=[0]
    i+=1
    w+=risoluzione
tmpx=assex[0]
tmpy=assey[0]
assex[n:n]=[tmpx]
assey[n:n]=[tmpy]

pl.plot(assex,assey,label="Radici di z")
pl.plot(x,y1,color='red')
pl.plot(x,y2,color='red')
pl.plot(riga,zero,color='black')
pl.plot(zero,riga,color='black')

print("Le radici n-esime (",n,") di z sono:")
for i in range(0,len(assex)-1):
    if assex[i]<0:
        assey[i:i]=[-1*assex[i]]
        print("w",i,": ",assex[i],"\t-i",assey[i])
    else:
        print("w",i,": ",assex[i],"\t+i",assey[i])

pl.show()
