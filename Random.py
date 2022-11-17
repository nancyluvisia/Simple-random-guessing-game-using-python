import random
import sys
print("The Random Number Guessing Game With Only Ksh 50".upper())
print("")
print("The winner takes away 10000 :)".upper())
prize=10000
print("")
number=random.randint(100,170)
print("What's your name")
name1=input("Enter first name : ")
name2=input("Enter surname : ")
ans=input("Do you want to play the game ?yes/no: ")
if ans =='yes':
    print(f"welcome {name1} {name2} wishing you luck".capitalize() )
    amount=int(input("Enter amount here : "))
    if amount>50:
         balance=amount-50
         print(f"successful payment your accnt balance is {balance}")
    elif amount==50:
        print("successful payment,proceed ")
    else:
        balance=50-amount
        print("insufficient amount,cannot proceed")
        print(f"your account balance is {amount},top up with {balance} to play")
        sys.exit()
       
else:
    sys.exit()
count=0
trials=3
while count<=2:
    user=int(input("Enter any  random number : "))
    count=count+1
    trials=trials-1
    if user>number:
        print(f"oops!!your number is above,try again\n{trials} trials remaining")
       
    elif user<number:
        print(f"oops!!your number is below ,try again\n{trials} trials remaining")
       #piu print(f"the number is {number}")       
    elif user==number:
        total=prize+amount
        print(f"Hurray!! ,,you won 10000 your accunt balance is {total} ")
        break
        
    else:
        sys.exit()

