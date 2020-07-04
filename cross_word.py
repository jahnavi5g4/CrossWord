r,c = list(map(int,input().split()))
s2d = []
for i in range(r):
    s = input()
    s2d.append(s)
ctr = 1
n = [[0 for x in range(c+1)]for y in range(r+1)]
for j in range(c):
    if s2d[0][j]!="*":
        n[0][j] = ctr
        ctr = ctr+1
    else:
        n[0][j]=-1
print(n)
for i in range(1,r):
    for j in range(c):
        if s2d[i][j] == "*":
            n[i][j]=-1
        if j==0 and s2d[i][j]!="*":
            n[i][j] = ctr
            ctr = ctr+1
        elif s2d[i][j]!="*":
            if (s2d[i][j-1]=="*" or s2d[i-1][j] == "*"):
                n[i][j] = ctr
                ctr = ctr+1
        
lr = []
for i in range(r):
    l = []
    for j in range(c):
        if s2d[i][j]!="*":
            l.append(s2d[i][j])
        else:
            if l!=[]:
                lr.append(l)
            l=[]
        if j == c-1 and s2d[i][j]!="*":
            if l !=[]:
                lr.append(l)
            l=[]
nr = []
for i in range(r):
    f = 0
    for j in range(c):
        if n[i][j]!=-1 and n[i][j]!=0 and f == 0:
            f = 1
            nr.append(n[i][j])
        if n[i][j] == -1:
            f = 0
print("ACROSS")
for i in range(len(nr)):
    print(nr[i],end = ".")
    for j in range(len(lr[i])):
        print(lr[i][j],end = "")
    print()
lc = []
for i in range(c):
    l = []
    for j in range(r):
        if s2d[j][i]!="*":
            l.append(s2d[j][i])
        else:
            if l!=[]:
                lc.append(l)
            l=[]
        if j == r-1 and s2d[j][i]!="*":
            if l !=[]:
                lc.append(l)
            l=[]
nc = []
for i in range(c):
    f = 0
    for j in range(r):
        if n[j][i]!=-1 and n[j][i]!=0 and f == 0:
            f = 1
            nc.append(n[j][i])
        if n[j][i] == -1:
            f = 0
d = {}
for i in range(len(nc)):
    d.update({nc[i]:lc[i]})
print("DOWN")
for i in sorted (d) : 
    print (i, end =".")
    for j in range(len(d[i])):
        print(d[i][j],end = "")
    print()
