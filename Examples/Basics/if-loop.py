from random import randint

x=randint(0,100);
print ("the value of x is between 1-100, let's find out more...")
if x < 50:
    print ("the value of x is less than 50")
elif x >50:
    print ("the value of x is more than 50")
else:
    print ("the value of x is exactly 50, woo!!")

print (x)
