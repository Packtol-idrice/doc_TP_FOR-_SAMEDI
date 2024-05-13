import math
def verif():
   m=int(input("entrer la taille du tableau"))
   if(m<0 or m>500):
     verif()
   return m
xi=[]
ni=[]
ec=[]
fc=[]
freqCum=[]
M=[]
vx=[]
mod=[]
tableau=[]
def TrieInsertion(t,n):
   i=0
   while (i<n):
      j=i-1
      while(j>=0 and t[j]>t[j+1]):
         t[j],t[j+1]=t[j+1],t[j]
         j=j-1
      i+=1
   return t
def dataxi(t,n):
   i=0
   while (i<n):
      dataXi=[int(input("entrer les xi"))]
      t=t+dataXi
      i=i+1
   TrieInsertion(t,n)
   return t
def datani(t,n):
   i=0
   while (i<n):
      dataNi=[int(input("entrer les Ni"))]
      t=t+dataNi
      i=i+1
   return t
def totalNi(t,n):
   i=0
   s=0
   while (i<=n-1):
      s=s+t[i]
      i=i+1
   return s
def ecc(t,f,n):
    s=0
    i=0
    while (i<n):
       s=s+t[i]
       f+=[s]
       i+=1
    return f
def freq(t,f,n):
   total=totalNi(t,n)
   i=0
   while (i<n):
      s=t[i]/total
      f+=[s]
      i+=1
   return f
def fcc(t,tr,n):  
   s=0
   i=0
   while (i<n):
      s=s+t[i]
      tr+=[s]
      i+=1
   return tr
def moy(t,tb,n):
   i=0
   s=0
   moy=0
   while (i<n):
      s+=(t[i]*tb[i])
      i+=1
   m=totalNi(tb,n)
   moy=s/m
   return moy
def med(t,n):
    y=n/2
    if n%2==0: 
      return y
    else:
      xm=n/2
      med=(t[xm]+t[xm +1])/2
    return med
def compte(t,n):
   i=0
   while(i<n):
      print(i)
      i+=1
def Quartile(t,tb,f,n):
   total=totalNi(tb,n)
   pk=(0.25*total)
   pkk=(0.5*total)
   pkkk=(0.75*total)
   ec=ecc(t,f,n)
   i=0
   b=0
   c=0
   j=0
   m=0
   p=0
   while (i<n):
      if (ec[i]<=pk):
         j=i
      i+=1
      break
   q1=t[j]
   while (b<n):
      if (ec[b]<=pkk):
         m=b
         break
      b+=1
      break
   q2=t[m]
   while (c<n):
      if (ec[c]<=pkkk):
         p=c
         break
      c+=1
      break
   q3=t[p]
   q=q3-q1
   print ("quartile q1=",q1,"quartile q2=",q2,"quartile q3=",q3,"interquartile=",q)
def variance(t,tb,n):
   i=0
   s=0
   j=0
   p=0
   Xbar=moy(t,tb,n)
   while(i<n):
      s+=((t[i]-Xbar)*(t[i]-Xbar))
      i+=1
   while(j<n):
      p+=(tb[j]*s)
      j+=1
   total=totalNi(tb,n)
   var=p/total
   return var 
def acartType(t,tb,n):
   var=variance(t,tb,n)
   ecartT=math.sqrt(var)
   return ecartT
def etendu(t,n):
   i=0
   e=0
   ti=t[0]
   p=t[n-1]
   e=p-ti
   return e 
def coefV(t,tb,n):
   vx=variance(t,tb,n)
   Xbar=moy(t,tb,n)
   coef=vx/Xbar
   return coef
def maximum(tb,n):
   i=1
   m=tb[0]
   while (i<n):
      if m<tb[i]:
         m=tb[i]
      i+=1
   return m
def recherche(tb,n):
   rech=maximum(tb,n)
   i=0
   j=0
   while (i<n):
      if rech==tb[i]:
         j=i
         break
      i+=1
   return j
def MOde(t,tb,mod,n):
   cherche=recherche(tb,n)
   i=0
   while(i<n):
      s=t[cherche]
      Lmod=mod+[s]
      i+=1
   return Lmod
def show(xi,ni,ec,fc,fcc,M,tab,n):
    modalite=dataxi(xi,n)
    eff=datani(ni,n)
    cc=ecc(eff,ec,n)
    totalNI=totalNi(eff,n)
    moyenne=moy(modalite,eff,n)
    frequence=freq(eff,fc,n)
    Fcumul=fcc(frequence,freqCum,n)
    varian=variance(modalite,eff,n)
    ecart=acartType(modalite,eff,n)
    cofvar=coefV(modalite,eff,n)
    lemode=MOde(modalite,eff,mod,n)
    etan=etendu(modalite,n)
    mde=med(ni,n)
    def prin(t,n):
       p=0
       while(p<n):
          print(t[p],end="  ")
          p+=1
    print("1-les modalites et les effectifs sont:")
    prin(modalite,n)
    print("\n")
    prin(eff,n)
    print("\n")
    print("2-les effectifs cumule:")
    prin(cc,n)
    print("\n")
    print("les frequence")
    prin(frequence,n)
    print("\n")
    print("3-les frequences cumules croissant sont")
    prin(Fcumul,n)
    print("\n")
    print("4-la mediane est",mde)
    print("\n")
    print("5-la variance est ",varian)
    print("\n")
    print("5-la variance est ",varian)
    print("\n")
    print("6-l'ecart type est ",ecart)
    print("\n")
    print("7-le coef de variation est ",cofvar)
    print("\n")
    print("8-le mode est ",lemode)
    print("\n")
    print("9-l'etandu est ",etan)
    print("\n")
    Quartile(modalite,eff,ec,n)

#b) variable continue
densite=[]
cumuler=[]
xi=[]
ni=[]
ec=[]
Tx=[]
Ty=[]
Tni=[]
Tamp=[]
centre=[]
stk=[]
def dataXi(t,n):
   i=0
   while (i<n):
        dataXi=[int(input("entrer les xi minimum"))]
        t+=dataXi
        i+=1
   return t
def dataYi(t,n):
   i=0
   while (i<n):
        dataXi=[int(input("entrer les xi maximum"))]
        t+=dataXi
        i+=1
   return t
def amplitude(t1,t2,tb,n):
   i=0
   while (i<n):
      ai=t2[i]-t1[i]
      tb+=[ai]
      i+=1
   return tb   
def datani(t,n):
    i=0
    while (i<n):
        dataNi=[int(input("entrer les Ni"))]
        t+=dataNi
        i+=1
    return t
def densit(t1,t2,teff,tamp,new_dense,n):
   total=totalNi(teff,n)
   i=0
   d=0
   while (i<n):
      d=teff[i]/tamp[i]
      new_dense+=[d]
      i+=1
   return new_dense
def classeModal(t1,t2,tb,n):
    maxi=maximum(tb,n)
    search=recherche(tb,n)
    cls_modal=[t1[search],t2[search]]
    return cls_modal
def mode(t1,t2,tb,ai,dcc,n):
   maxi=maximum(dcc,n)
   i=0
   while (i<n):
      if (dcc[i]<=maxi):
         j=i+1
      i+=1
   print(dcc)
   d1=dcc[j-1]-dcc[j]
   d2=dcc[j]-dcc[j-1]
   d=d1+d2
   print("d:",d,"d1:",d1,"d2:",d2)
   mod=t1[j]+(ai[j]*(d1/d))
   return mod

def center(t1,t2,new,n):
   i=0
   ci=0
   while (i<n):
      ci=(t1[i]+t2[i])/2
      new+=[ci]
      i+=1
   return new
def quartile(t1,t2,tb,cumu,n):
   total=totalNi(tb,n)
   pk=(0.25*total)
   print("pk=",pk)
   pkk=(0.5*total)
   pkkk=(0.75*total)
   i=0
   b=0
   c=0
   j=0
   m=0
   p=0
   f=0
   while (i<n):
      if (cumu[i]<=pk):
         j=i+1
        # st=st+[cumu[j]]
      i+=1
   Fqa1=cumu[j-1]
   Fqa2=cumu[j]
   FqA2=cumu[j+1]
   qa1=t1[j]
   qa2=t2[j]
   #print("pk=",pk,"Fcumul(j)",Fqa1,"Fcumul(j-1)",Fqa2,"Fcumul(j+1)",FqA2,"cumuler=")
   #print("pk=",pk,"ximin(j)",qa1,"ximax(j)",qa2)
   q1=qa1+((pk - Fqa1)*((qa2 - qa1)/(FqA2 - Fqa2)))
   print("quartile q1:)=   ",q1)
   while (b<n):
      if (cumu[b]<=pkk):
         m=b+1
      b+=1
   Fqaa1=cumu[m-1]
   Fqaa2=cumu[m]
   FqaA2=cumu[m+1]
   qaa1=t1[m]
   qaa2=t2[m]
   #print("pk=",pkkk,"Fcumul(j-1)",Fqaa1,"Fcumul(j)",Fqaa2,"Fcumul(j+1)",FqaA2)
   #print("pk=",pk,"ximin(j)",qaa1,"ximax(j)",qaa2)
   q2=qaa1+((pkk - Fqaa1)*((qaa2 - qaa1)/(FqaA2 - Fqaa2)))
   print("quartile q2:)=   ",q2)
   while (c<n):
      if (cumu[c]<=pkkk):
         p=c+1
      c+=1
   Fqaaa1=cumu[p-1]
   Fqaaa2=cumu[p]
   FqaaA2=cumu[p+1]
   qaaa1=t1[p]
   qaaa2=t2[p]
   #print("pk=",pkkk,"Fcumul(j-1)",Fqaaa1,"Fcumul(j)",Fqaaa2,"Fcumul(j+1)",FqaaA2)
   #print("pk=",pk,"ximin(j)",qaaa1,"ximax(j)",qaaa2)
   
   q3=qaaa1+((pkkk - Fqaaa1)*((qaaa2 - qaaa1)/(FqaaA2 - Fqaaa2)))
   print("quartile q3:)=   ",q3)
   q=q3-q1
   print("l'inter-quartile q est   :)=",q)
def show2(t1,t2,ts,ta,cu,de,cent,n):
   def prin(t,n):
      p=0
      while(p<n):
         print(t[p],end="  ")
         p+=1
   dxi=dataXi(t1,n)
   dyi=dataYi(t2,n)
   dni=datani(ts,n)
   ec=ecc(ts,cu,n)
   Amp=amplitude(t1,t2,ta,n)
   clsM=classeModal(t1,t2,ts,n)
   dense=densit(t1,t2,ts,ta,de,n)
   ci=center(t1,t2,cent,n)
   vx=variance(cent,dni,n)
   moyenne=moy(cent,dni,n)
   varian=variance(cent,dni,n)
   ecart=acartType(cent,dni,n)
   cofvar=coefV(cent,dni,n)
   Mo=mode(t1,t2,ts,ta,de,n)
   print("1-les modalites minimum et maximal + les et effectifs\n")
   prin(dxi,n)
   print("\n")
   prin(dyi,n)
   print("\n")
   prin(dni,n)
   print("\n")
   print("2-les valeurs centrales")   
   prin(ci,n)
   print("\n")
   print("3-les amplitudes")
   prin(Amp,n)
   print("\n")
   print("4-les effectifs cumuler")
   prin(ec,n)
   print("\n")
   print("5-les densites ")
   prin(dense,n)
   print("\n")
   print("6-les valeus de  tendances centrales")
   print("\n")
   print("\t","6-1)la moyenne:)  ",moyenne)
   print("\n")
   print("\t","6-2)la variance:)  ",vx)
   print("\n")
   print("\t","6-3)le mode est de :",Mo)
   print("\n")
   print("\t","6-4)la classe modale",clsM)
   print("\n")
   print("7-les caracteristiques de dispertions:)")
   print("\t","7-1)l'ecart type est :)",ecart)
   print("\n")
   print("\t","7-2)le coeffiscients de correlation :)  ",cofvar)
   print("\n")
   print("\t","7-1)les quartilles :)  ")
   quartile(t1,t2,ts,ec,n)
def debut():
   print(" \n (1) pour le menu statistique a variable discrete ou alors : )\n")
   print("    (2) pour les variables statistique continue \n")
   x=int(input("entrer le choix de votre proposition   :)"))
   print("\n")
   if(x==1):
      n=verif()
      show(xi,ni,ec,fc,fcc,M,tableau,n)
      debut()
   elif(x==2):
      n=verif()
      show2(Tx,Ty,Tni,Tamp,cumuler,densite,centre,n)
      debut()
   else:
      print("bien renseigner le nombre saisie or positif alternate number")
      debut()
debut()         
       
