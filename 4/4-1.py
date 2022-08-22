import time

n = int(input())

plans = list(input().split())
start = time.time()
x=1
y=1

for i in range (len(plans)):
    if plans[i] == 'R' and x<n:
            x += 1
    elif plans[i] == 'L' and x>1:
            x -= 1
    elif plans[i] == 'U' and y>1:
            y -= 1
    elif plans[i] == 'D' and y < n:
            y +=1

print ("time :", time.time()-start )
print(y,x)
