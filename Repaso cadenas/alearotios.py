import os
from random import randint as rn
doc=1
while(doc==1):
    os.system("cls")
    n1=rn(1,10)
    n2=rn(1,10)
    print(n1)
    print(n2)
    if n1>n2:
        print(n1," es mayor")
    elif n2>n1:
        print(str(n2)+" es mayor")
    else:
        print(str(n1) + "=" + str(n2))
    doc=input("ya xd: ")

    
