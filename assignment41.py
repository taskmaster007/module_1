import random
print("Press enter to roll dice and q to quit")
a = input()
while(a != 'q'):
    x = random.randrange(1,7)
    print(x)
    a = input()