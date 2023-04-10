n=1260
coinType = {500,100,50,10}
index = 0

while(True):
    if n-coinType[index]>0:
        n-=coinType[index]
    else :
        break;
