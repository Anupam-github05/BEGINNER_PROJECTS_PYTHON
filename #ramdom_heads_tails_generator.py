#ramdom_heads_tails_generator
import random
c = 1
while c == 1:
    number = random.randint(1, 100)
    if number % 2 == 0:
        print ("HEADS!")
    else:
        print ("TAILS!")
    c = int (input ("Press 1 to continue and 0 to exit "))
    if c == 0:
        print ("Terminating program")
    elif type (c) != int or (c!= 1 and c!= 0):
        print ("Wrong input! Terminating program")
        c= 2
    else:
        continue