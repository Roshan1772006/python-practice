a=[35,19,11,10,9,61,52,5]
b=0
for i in a:
    b+=1
print(b)
print("Before change\n",a)
for j in range (b):
    for i in range(b-1):
        if (a[i]>=a[i+1]):
            temp=a[i+1]
            a[i+1]=a[i]
            a[i]=temp
print("after the change\n",a)    

