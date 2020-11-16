import numpy as np
import datetime as dt

def backtrace(s1,i): #Function to do percolate sorting from bottom to top (percolate up)
    j=int((i-1)/2)
    while j>=0 and s1[i]>s1[j]:
        s1[i],s1[j]=s1[j],s1[i]
        i=j
        j=int((i-1)/2)
i=len(s1)-1
j=len(s1)
sor_arr=[]
print(dt.datetime.now())
s1=np.random.permutation(100)#To create a np object of random numbers from 0 to 99
s1=list(s)#To convert the np object to list
print("Elements before sorting:",s1)

while j>0:
    while i>0:
        backtrace(s1,i)
        i-=1
    sor_arr.append(s1.pop(0))
    i=len(s1)-1
    j=len(s1)

print(dt.datetime.now())
print("Elements after sorting:",sor_arr)