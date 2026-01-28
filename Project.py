import pandas as pd
f=[86,45,14,5]
Series=pd.Series(f)
print(Series.dtype)
print()
dictionary={1:2,2:3,3:4,4:5}
df=pd.DataFrame(dictionary,index=[1,2,3,4])