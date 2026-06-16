# loops basic example
# printing numbers from 1 to 5
# while loop executes output until the condition becomes false 
for i in range(1,6):
    print(i)

# i+=1 equal to i=i+1


# for loops for list 
l = [1,"todo","Harry","Pranay","Dynamight"]
i = 0

while(i<len(l)):
    print(l[i])
    i+=1

l = [1,2,3,4,5]

for i in l:
    print(i)

# for loops with Tuples
t=(6,1,8,78,20)
for i in t:
    print(i)

# for loop with string
s="Harry"
for i in s:
    print(i)

# use of "else" in for loop (imp for interview)
a = [1,7,9]
for item in a:
    print(item)

else:
    print("Done") #This is printed when loop exhausts!

# use of break and continue in for loop 
for i in range(10):
    if(i==5):
        break #Exit the loop
print(i)
























