'''a=1
b=5.22
c='harry'
d=False
e=None'''
num='*'
list=[5,4,3,2,1]
for i in list:
    i*=num
    print(i)



# Multipication of the table
table=1
num=int(input("Enter a number :"))      
for i in range(1,11):
    if num!=0:
        
        print(num," X ",i," = ",i*num)
    
    else:
        print("Please enter a number greater than 0")
        break
#reverse star pattern 5
num='*'
for i in range(1,11,-1):
    i*=num
    print(i)
def Addition(num1,num2):
    print(num1+num2)

def Subtraction(num1,num2):
    print(num1-num2)

def Multiplication(num1,num2):
    print(num1*num2)

def divsion(num1,num2):
    print(num1/num2)

def Module(num1,num2):
    print(num1%num2)

def calculator():
    while True:
            print("Choice any of the option")
            print("1.Addition")
            print("2.Subtraction")
            print("3.Multiplication")
            print("4.division")
            print("5.Module")
            print("6.Exit")
            num=int(input("Enter Your chice :"))
            if num==1:
                num1=int(input("Enter a number :"))
                num2=int(input("Enter a number :"))
                Addition(num1,num2)
                
    
            elif num==2:
                num2=int(input("Enter a number :"))
                num1=int(input("Enter a lager number than first number :"))
                Subtraction(num1,num2)

            elif num==3:
                num1=int(input("Enter a number :"))
                num2=int(input("Enter a number :"))
                Multiplication(num1,num2)

            elif num==4:
                num1=int(input("Enter a number :"))
                num2=int(input("Enter a larger number than first number :"))
                divsion(num1,num2)

            elif num==5:
                num1=int(input("Enter a number :"))
                num2=int(input("Enter a lager number than first number :"))
                Module(num1,num2)
    
            elif num==6:
                break

            else:
                print("Input  is Invalid in the software")

calculator()

