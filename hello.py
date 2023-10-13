'''
Created on 2023/10/13

@author: t21cs014
'''
print("Hello, Python world")
print("この文を変更しました")
a=10
b=0.000001
c='string'
print(a,b,c)

for x in{1,2,3}:
    print(x)

if 0<x<10:
    print('0<x<10')
else:
    print('x=<0,x>=0')

p=0
while p<10:
    print('p=',p)
    p+=1

import  math

print(type(math))
print(math)

print(math.pi)

from fibonacci import fibo

print(fibo(20))

from sort import quick_sort

DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

print(f"{DATA} → {quick_sort(DATA)}")

from janken import main
main()