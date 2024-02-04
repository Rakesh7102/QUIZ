print("WELCOME TO QUIZ")
print()
print("Choose the correct option (A, B, C, or D) from Each Question.")

def qz(n,c):
    if n==1:
        print()
        print("1) What is the capital of the Indian state of Maharashtra?")
        print()
        print('''Options are:     
    A) Chennai

    B) Kolkata

    C) Mumbai

    D) Hyderabad''')
        print()
        
        ans=input("Enter Option A, B, C or D : ")
        print()
        ans=ans.upper()
        if ans=='C':
            print("Mumbai is the right answer :)")
            print()
            c+=1
        elif ans=='A' or ans=='B' or ans=='D':
            print("Wrong answer :(")
            print()
            print("The correct answer is Mumbai")
        else:
            print("Please Enter only A, B, C or D")
            qz(n,c)

    if n==2:
        print()
        print("2) What is the capital of the Indian state of West Bengal?")
        print()
        print('''Options are:     
    A) Chennai

    B) Kolkata

    C) Mumbai

    D) Hyderabad''')
        print()
        
        ans=input("Enter Option A, B, C or D : ")
        print()
        ans=ans.upper()
        if ans=='B':
            print("Kolkata is the right answer :)")
            c+=1
        elif ans=='A' or ans=='C' or ans=='D':
            print("Wrong answer :(")
            print()
            print("The correct answer is Kolkata")
        else:
            print("Please Enter only A, B, C or D")
            qz(n,c)
    
    if n==3:
        print()
        print("3) What is the capital of the Indian state of Tamil Nadu?")
        print()
        print('''Options are:     
    A) Chennai

    B) Kolkata

    C) Mumbai

    D) Hyderabad''')
        print()
        
        ans=input("Enter Option A, B, C or D : ")
        print()
        ans=ans.upper()
        if ans=='A':
            print("Chennai is the right answer :)")
            c+=1
        elif ans=='B' or ans=='C' or ans=='D':
            print("Wrong answer :(")
            print()
            print("The correct answer is Chennai")
        else:
            print("Please Enter only A, B, C or D")
            qz(n,c)
    
    if n==4:
        print()
        print("4) What is the capital of the Indian state of Telengana?")
        print()
        print('''Options are:     
    A) Chennai

    B) Kolkata

    C) Mumbai

    D) Hyderabad''')
        print()
        
        ans=input("Enter Option A, B, C or D : ")
        print()
        ans=ans.upper()
        if ans=='D':
            print("Hyderabad is the right answer :)")
            c+=1
        elif ans=='A' or ans=='C' or ans=='B':
            print("Wrong answer :(")
            print()
            print("The correct answer is Hyderabad")
        else:
            print("Please Enter only A, B, C or D")
            qz(n,c)
        
    return c

c=0
for i in range(1,5):
    c= qz(i,c)

print()
print("Your total Score is : ",c)

        




