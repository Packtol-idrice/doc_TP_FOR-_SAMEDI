# TAGNE TALLA IDRISS 19M2351
# KALEFACK PAVEL 19M2583
# MEVOH NYEBE LOGOPHILE DIVIN 20U2794
# LUKONG ASA BRANDON 19M2516

import math
import matplotlib.pyplot as plt
# on importe les bibliotheque neccessaire
def verif():
   m=int(input("entrer la taille du tableau :) "))
   if(m<0 or m>500):
     verif() 
   return m
# la fonction verif est la fonction utiliser pour entrer la taillle du tableau
# la fonction verif est rappeller dans le cas ou l'on entrer une valeur du tableau negatif
t1=[]
# creation du tableau des effectifs en x
t2=[]
# creation du tableau des effectif en y
tni=[]
# creation du tableau des effectifs 
pred=[]
# le tableau des prediction lors de la regression pour stoquer les yi(predict)
m=[]

def dataxi(t,n):
   i=0
   while (i<n):
      t+=[int(input(" entrer les xi "))]
      i=i+1
   return t
# fonction pour les donnees en  xi
#cette fonction stoque les donnees dans le tableau t1
def datayi(t,n):
   i=0
   while (i<n):
      t+=[int(input(" entrer les yi "))]
      i=i+1
   return t
# fonction pour les donnees en  yi
# cette fonction stoque les donnees dans le tableau t2
def datani(t,n):
   i=0
   while (i<n):
      t+=[int(input(" entrer les Ni "))]
      i=i+1
   return t
# la focntions pour stoquer les donnees du tableau (les effectifs )
# stoque les donnees dans le tableau des tni 
def totalNi(t,n):
   i=0
   s=0
   while (i<=n-1):
      s+=t[i]
      i=i+1
   return s
# la fonction totalni utuiliser pour avoir le total des effecifs
# cette fonction resort le total des effectifs
def moy(t,tb,n):
   i=0
   s=0
   moy=0
   while (i<=n-1):
      s+=(t[i]*tb[i])
      i+=1
   m=totalNi(tb,n)
   moy=s/m
   return moy
# le calcule des moyennes
# cette fonction calcules les moyennes 
def variance(t,tb,n):
   i=0
   s=0
   j=0
   p=0
   Xbar=moy(t,tb,n)
   while(i<=n-1):
      s+=((tb[i])*((t[i]-Xbar)*(t[i]-Xbar)))
      i+=1
   total=totalNi(tb,n)
   var=s/total
   return var
# fonction qui calcul les variances
def somErreur(t,tb,n):
   i=0
   s=0
   j=0
   p=0
   totalReduit=totalNi(tb,n)-2
   Xbar=moy(t,tb,n)

   while(i<=n-1):
      s+=(((t[i]-Xbar)*(t[i]-Xbar)))
      i+=1
   total=totalNi(tb,n)
   var=s/total
   return var

# calcul des variances
def acartType(t,tb,n):
   var=variance(t,tb,n)
   ecartT=math.sqrt(var)
   return ecartT
# calcul des ecart-type

def covariance(tx,tni,ty,n):
   xbar=moy(tx,tni,n)
   ybar=moy(tx,tni,n)
   total=totalNi(tni,n)
   i=0
   cov=0
   while(i<n):
      cov+=(tx[i]-xbar)*(ty[i]-ybar)
      i+=1
   result=cov/total
   return result
# fonction qui calcul les covariances 
def pente(tx,tni,ty,n):
   cov=covariance(tx,tni,ty,n)
   Vx=variance(tx,tni,n)
   return cov/Vx
# calcul de la pente
def ordonnee(tx,tni,ty,n):
   xbar=moy(tx,tni,n)
   ybar=moy(ty,tni,n)
   alpha=pente(tx,tni,ty,n)
   return (ybar)-(alpha*(xbar))
#calcul des ordonees a l'origine dans la droite de regression (yi=ax+b)=>correspond a b
def correlation(t1,tni,t2,n):
   cov=covariance(t1,tni,t2,n)
   EcartX=acartType(t1,tni,n)
   EcartY=acartType(t2,tni,n)
   return cov/(EcartX*EcartY)
# fonction qui calcul la correlation entre les donnees
def somPredict(tx,ty,tni,p,n):
   i=0
   s=0
   j=0
   som=0
   vxBar=0
   e=0
   vx=0
   sigExp=0
   testC=0
   totalReduit=totalNi(tni,n)-2
   Xbar=moy(tx,tni,n)
   a=pente(tx,tni,ty,n)
   b=ordonnee(tx,tni,ty,n)
   while(e<=n-1):
      vx+=((tx[e]-Xbar)*(tx[e]-Xbar))
      e+=1
   while(i<=n-1):
      p+=[((a*(tx[i]))+b)]
      #print('pi:',p[i])
      i+=1
   while(j<=n-1):
      som+=((ty[j]-p[j])*(ty[j]-p[j]))
      j+=1
   vxBar=som/totalReduit
   sigExp=math.sqrt(vxBar/vx)
   if(a<0):
      a=a*-1
   testC=(a/sigExp)
   print("valeur du test calculer de student ",testC)
   if(testC<2,228):
      print('on accepte l\'hypothese ho, la variable x exprime est significative et contribut a l\'explication de y')
   elif(testC<=2,306):
      print('on accepte l\'hypothese ho, la variable x exprime est significative et contribut a l\'explication de y')
   else:
      print("on refute l'hypothese ho, la variable n'est pas significative pour le contribuer a expliquer y")
   # return testC
def fisher(tx,ty,tni,p,n):
   j=0
   vxBar=0
   e=0
   vx=0
   vt=0
   vf=0
   testC=0
   totalReduit=totalNi(tni,n)-2
   Xbar=moy(ty,tni,n)
   while(e<=n-1):
      vx+=((ty[e]-Xbar)*(ty[e]-Xbar))
      e+=1
   while(j<=n-1):
      vt+=((p[j]*ty[j]-Xbar)*(p[j]*ty[j]-Xbar))
      j+=1
   vf=(vx/1)/(vt/totalReduit)
   testC=vf
   print("valeur du test calculer de fisher ",testC)
   if(testC<=3,33):
      print('on accepte l\'hypothese ho, les variables x et y sont independante')
   elif(testC<=3,20 and totalReduit>=10):
      print('on accepte l\'hypothese ho, les variables x et y sont independante')
   else:
      print('on accepte l\'hypothese ho, les variables x et y sont dependante')

   # return  vf
# fonction de fisher
def errTheo(tx,ty,tni,n):
   j=0
   som=0
   s=0
   i=0
   m=[]
   t=[]
   de=[]
   ki=[]
   ki2=[]
   rki=[]
   rki2=[]
   k=0
   jt=0
   tj=0
   f=0
   testC=0
   while(j<=n-1):
      som+=tx[j]
      s+=ty[j]
      t+=[s+som]
      # print('somx:',som,'somy:',s,'t[i]',t[j])
      j+=1
   while(i<=n-1):
      de+=[(s*t[i]/(s+som))]
      i+=1
   while(f<=n-1):
      ki+=[((tx[f]-de[f])*(tx[f]-de[f]))/de[f]]
      ki2+=[((ty[f]-de[f])*(ty[f]-de[f]))/de[f]]
      rki+=[tx[f]/ki[f]]
      rki2+=[ty[f]/ki2[f]]
      f+=1
   while(k<=n-1):
      jt+=rki[k]
      tj+=rki2[k]
      k+=1
   # testC=(tj,jt)

   testC=jt+tj
   print("valeur du test calculer de khi-deux ",testC)
   if(testC<=16,91):
      print('on accepte l\'hypothese ho, les variables x et y sont independante')
   elif(testC<=19,67 and som>=10):
      print('on accepte l\'hypothese ho, les variables x et y sont independante')
   else:
      print('on accepte l\'hypothese ho, les variables x et y sont dependante')
def courbe(t1,t2):
       
   plt.plot(t1,t2,label='SANS LES DEUX STAGIARES')
   plt.title('avec les deux stagiares--ET sans les deux stagiaires ')
#  la fonctions plots et je passe mes tableau en parametres
   plt.scatter(t1,t2,c='green')
#  POUR LES NUAGES DE POINTS
   plt.xlabel('axe de A')
# je precise l'axe des x
   plt.ylabel('axe de B')
#  je precise l'axe des y
   plt.legend()
   plt.show() 
   plt.plot(t1,t2,label='SANS TOUT LES STAGIAIRES') 
   plt.scatter(t1,t2,c='orange')
   # return (tj,jt)



def show(t1,t2,tni,pred,n):
   # ici  je recupere les fonctions et j'appelle
    xi=dataxi(t1,n)
    yi=datayi(t2,n)
    eff=datani(tni,n)
    moyenneXi=moy(t1,tni,n)
    moyenneYi=moy(t2,tni,n)
    Vx=variance(t1,tni,n)
    Ex=acartType(t1,tni,n)
    Vy=variance(t2,tni,n)
    Ey=acartType(t2,tni,n)
    alpha=pente(t1,tni,t2,n)
    cov=covariance(t1,tni,t2,n)
    ordonee=ordonnee(t1,tni,t2,n)
    correlate=correlation(t1,tni,t2,n)
   #  ecartBAR=somPredict(t1,t2,tni,pred,n)
   #  erthe,er=errTheo(t1,t2,tni,n)
   #  vf=fisher(t1,t2,tni,pred,n)
    def prin(t1,n):
       p=0
       while(p<n):
          print(t1[p],end="  ")
          p+=1
    print("1-les modalites et les effectifs sont:")
    print("\n")
    prin(xi,n)
    print("\n")
    prin(yi,n)
    print("\n")
    prin(eff,n)
    print("\n")
   #  ICI j'adopte un mode d'affichage qui affiches les tableaux (modalite en xi,modalite en yi,effectifs)
    print("la variance en x est ",Vx)
    print("\n")
    print("la variance en y est ",Vy)
    print("\n")
    print("'ecart type est ex::>",Ex,"/ey::>",Ey)
    print("\n")
    print("'la  moyenne est  mx::>",moyenneXi,"/my::>", moyenneYi)
    print("\n")
    print("'la  covariance  est ::>",cov)
    print("\n")
    print("'la  pente  est ::>",alpha)
    print("\n")
    print("'la  ordonnee  est ::>",ordonee)
    print("\n")
    print("'y ::>",alpha,'X+',ordonee)
    print("\n")
    print("\n")
    print("'correlation  est  ::>",correlate)
    print('10-la valeur de student exprimer est de:>',)
    somPredict(t1,t2,tni,pred,n)
    print('11-la valeur de khi caree exprimer est de:>',)
    errTheo(t1,t2,tni,n)
    print( '12-valeur de fisher exprimer est de ',)
    fisher(t1,t2,tni,pred,n)
   #  ici j'appelle tout les resultats des operations des differentes lois et je les affiches 


def debut():
   print(" \n (valider (1) pour accerpter d'effectuer l'etude statistique) : )\n")
   x=int(input("entrer le choix de votre proposition  :) "))
   print("\n")
   if(x==1):
      n=verif()
      show(t1,t2,tni,pred,n)
      courbe(t1,t2)
      n=verif()
      show(t1,t2,tni,pred,n)
      courbe(t1,t2)
    #  plt.scatter(t1,t2,c='green')
   #  POUR LES NUAGES DE POINTS
     # plt.xlabel('axe de A')
   # je precise l'axe des x
      #plt.ylabel('axe de B')
   #  je precise l'axe des y
      #plt.show()
      
      debut()
   elif(x==2):
      debut()
   else:
      print("bien renseigner le nombre saisie or positif alternate number")
      debut()
debut()         