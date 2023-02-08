import numpy as np
n=2# no.of traits observed
x1=input()#dominant of 1st trait
x2=input()#recursive of 1st trait
y1=input()#dominant of 2nd trait
y2=input()#recursive of 2nd trait
#to produce F1 generation Cross Complete Dominant and Complete recursive
#trait x & y:
print("F1 Generation")
f1=x1+x2+y1+y2
print(f1)
f_1=f1
print(f_1)
print("Segregation of Alleles")
l_f1=[]
for i in range(len(f1)):
    l_f1.append(f1[i])
l_f_1=[]
for i in range(len(f_1)):
    l_f_1.append(f1[i])
print(l_f1,l_f_1)
print("F2 Generation")
F2_pos=[l_f1[i]+l_f_1[j] for j in range(len(l_f_1)) for i in range (len(l_f1))]
print(F2_pos)#possible combinations
f2p=[]#most likely to happen combination
for i in range(len(F2_pos)):
    c1=F2_pos[i][0].lower()
    c2=F2_pos[i][1].lower()
    if(c1!=c2):
        f2p.append(F2_pos[i])
    else:
        continue
print(f2p) # possible traits both parents
F2_P1=[]
F2_P2=[]
mid=len(f2p)//2
#Traits of parent 1
for x in range(0,mid):
    F2_P1.append(f2p[x])
#Traits of parent 2
for x in range(mid,len(f2p)):
    F2_P2.append(f2p[x])
print("\n")
print("Parent of F2 generation As Alleles")
print(F2_P1,F2_P2)
# All possible Children in f2
print("\nChildren of F2\n")
F2_c=[F2_P1[i]+F2_P2[j]for j in range(len(F2_P2)) for i in range(len(F2_P1))]
print(F2_c)
# in Matrix Form
res=np.array(F2_c).reshape(mid,mid)
print("\nPunnett Square of F2\n")
print(res,end=" ")

