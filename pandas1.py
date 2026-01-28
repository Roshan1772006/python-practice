import pandas as pd
import numpy as np
s1= pd.Series([1,2,3,4,5,6])
print(s1)

# code 2

s2=pd.Series((1,2,3,4,5))
s3=pd.Series(['a','b','c','d'])
print('Series Object 02:')
print(s2)
print('Series Object 03:')
print(s3)

# code3

nda1 = np.arange(3,13,3.5)
print(nda1)
ser1=pd.Series(nda1)
print(ser1)

# code 4 using of linspace
s6 = pd.Series(np.linspace(24,64,5))
print(s6)
 
 # code 5 using of tile
s7= pd.Series(np.tile([3,5],2))
print(s7)
 
 #using of dictionary
stu={"a":39,"b":41,"c":42,"d":44}
s8 = pd.Series(stu)
print(s8) 

#using of index and value
s10 = pd.Series(5000,index=['Qtr1','Qtr2','Qtr3','Qtr4','Qtr5'])
print(s10)

# additinal of none or nan
obj2=pd.Series([6.5,np.nan,2.34])
print(obj2)

# using of datatype 
arr=[56,98,46,76]
mon=['jan','feb','mar','april']
obj3=pd.Series(data=arr,index=mon,dtype=np.float64)
'''print(obj3)'''

#common attribute of series
print(obj3.index)
print(obj3.index.name)
print(obj3.values)
print(obj3.dtype)
print(obj3.shape)
print(obj3.nbytes)
print(obj3.ndim)
print(obj3.size)

print(obj3.hasnans)
print(obj3.empty)
print(obj3.name)