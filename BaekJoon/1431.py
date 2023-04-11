n=int(input())

serial_list={}

for i in range (n):
    serial=input()
    serial_list[serial]=len(serial)

serial_list=sorted(serial_list.items(), key=lambda x: x[1])

serial_sort=[]


for word, i in serial_list:
    print(i)
print(serial_list)