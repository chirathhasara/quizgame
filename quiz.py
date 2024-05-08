print("*******************Welcome To the Quiz Game*******************")
x=input("please enter you name:")
y=int(input("please enter your age:"))

print("welcome "+x+" to this quiz there will be 5 mcq question and each carrys 1 mark")
print()
z=input("would you like to enter this game:(yes/no)")

if z.lower()!="yes":
    quit()
else:
    print("all right "+x+" let's play this game")

sum=0
print()
print("1.What is the main function of the mitochondria in a cell? \nA) Cell division\nB) Energy production\nC) Waste removal\nD) Protein synthesis")
print()
a1=input("enter your answer:")
if a1.lower()=="b":
    print("congratulation you are correct")
    sum+=1
    print("your score is "+str(sum))
else:
    print("sorry wrong answer")
    print("your score is "+str(sum))

print()
print("2.Which of the following is NOT a renewable energy source?\nA) Solar\nB) Wind\nC) Coal\nD) Hydroelectric")
print()
a1=input("enter your answer:")
if a1.lower()=="a":
    print("congratulation you are correct")
    sum+=1
    print("your score is "+str(sum))
else:
    print("sorry wrong answer")
    print("your score is "+str(sum))

print()
print("3.What is the chemical symbol for water?\nA) O2\nB) H2O\nC) CO2\nD) NaCl")
print()
a1=input("enter your answer:")
if a1.lower()=="b":
    print("congratulation you are correct")
    sum+=1
    print("your score is "+str(sum))
else:
    print("sorry wrong answer")
    print("your score is "+str(sum))

print()
print("4.What type of galaxy is the Milky Way?\nA) Spiral\nB) Elliptical\nC) Irregular\nD) Lenticula")
print()
a1=input("enter your answer:")
if a1.lower()=="a":
    print("congratulation you are correct")
    sum+=1
    print("your score is "+str(sum))
else:
    print("sorry wrong answer")
    print("your score is "+str(sum))

print()
print("5.Which organ in the human body produces insulin?\nA) Liver\nB) Pancreas\nC) Kidney\nD) Brain")
print()
a1=input("enter your answer:")
if a1.lower()=="b":
    print("congratulation you are correct")
    sum+=1
    print("your score is "+str(sum))
else:
    print("sorry wrong answer")
    print("your score is "+str(sum))

print()
print("*******************OK "+x+' you have succesfuly done the quiz***************************')
print("your final score is:"+str(sum))




