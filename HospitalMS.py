import pandas as pd
import numpy as np
def sign_in():
    #to be change before running the code
    print("Patient detail is added ")

def disase():
    if d==f: #d is disase and f is the data of doctor 
        print("this diseas can be ")
    else:
        print("this disase cannot be treated in this hospital")

def patient():
    print("doctor has added condition and detail about the Patient")

def Appointment():
    disase()
    if a == f:
        print("your appointment is book on date ,time ")

def discharge():
    if p in f:
        #delete the detail of the patient
        print("The discharge of the Patient is Successfull")
    else:
        print("The Patient is not is our hospital or check once again")



def Hospital():
    print("1.Are you Doctor")
    print("2.Are you Cilent")
    choice = int(input("Enter your choice "))
    if choice == 1:
        print("Detail of patient")
        print("Entering the condition of patient")
        choice= int(input("Enter your choice"))

    elif choice == 2:
        while True:
            print("1.sign in the account")
            print("2.Passent disase")
            print("3.Passent contion and information")
            print("4.Appointment To Doctor")
            print("5.Discharge of the passent")
            print("6.Exit")
            choice = int(input("Enter your choice = "))
            if choice == 1:
                print("sign in")
            elif choice == 2:
                print(patient)
            elif choice == 3:
                print("Patient")
            elif choice == 4:
                print("appointment")
            elif choice == 5:
                print("dicharge")
            elif choice == 6:
                print("THANK YOU FOR VISIT OUR HOSPITAL")
            else:
                print("invalid data for vaule")

Hospital()
        
