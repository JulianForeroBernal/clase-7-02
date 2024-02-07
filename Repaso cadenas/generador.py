import os

os.system("cls")
pintas=["picas","treboles","diamantes","corazones"]+[str(i)for i in range (2,11)]
valores=["A","J","Q","K"]
mazo=[(u,p) for u in valores for p in pintas]
for c in mazo:
    print(c)