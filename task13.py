def cube(x):
    return x *x*x
print(cube(2))
l = [1,2,4,6]
newl = list(map(cube,l))
print(newl)
#filter
def filter_function(a):
    return a>2
newnewl=list(filter(filter_function,l))
print(newnewl)
#reduce
from functools import reduce
numbers=[1,2,3,4,5]             # pehle 1+2=3 then 3+3=6 then 6+4=10 then 10+5=15
def mysum(x,y):
    return x+y
sum=reduce(mysum,numbers)
print(sum)
