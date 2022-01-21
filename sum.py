#program that takes an input N  and displays the odd sum and even sum:
n=int(input("Enter the Integer: \n"))
sumeven=0
sumodd=0
while(n!=0):
    digit=n%10
    n=n//10
    if(digit%2==0):
     sumeven+=digit
    else:
     sumodd+=digit

print("Sum of odd {}".format(sumodd))
print("Sum of Even {}".format(sumeven))
