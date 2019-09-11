import string

alpha = string.ascii_lowercase
n = int(input())

L = []

for i in range(n):
    s = '-'.join(alpha[i:n])
    L.append(s[::-1]+s[1:])
   
width = len(L[0])

dashes=int(width/2)

for i in range(n-1,0,-1):
    for j in range(dashes):print("-", sep='', end='', flush=True)
    print(L[i],end = "")
    for k in range(dashes):print("-",end="")
    print("")
    dashes = dashes-2
  

for i in range(n):
    for j in range(dashes,0,-1):print("-",end = "")
    print(L[i],end="")
    for j in range(dashes,0,-1):print("-",end = "")
    print("")
    dashes = dashes+2
