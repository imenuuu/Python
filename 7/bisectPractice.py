from bisect import bisect_left,bisect_right

a=[1,2,4,5,8]
x=5

print(bisect_left(a, x))
print(bisect_right(a,x))