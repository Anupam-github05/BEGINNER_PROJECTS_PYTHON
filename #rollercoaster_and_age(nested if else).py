#rollercoaster_and_age(nested if else) and multiple if
print ("Hello! Welcome to our roller coaster\n")
height = float (input ("Please enter your height in cms\n"))
if height >= 120:
    age = int (input ("Please enter your age! \n"))
    if age <= 12:
        print ("Your ticket will cost $5")
        tkt = 5
    elif age >12 and age <= 18:
        print ("Your ticket will cost $7")
        tkt = 7
    else:
        print ("Your ticket will cost $12")
        tkt = 12
    photo = input ("Do you want to have a photo take? Type y for yes and n for No ")
    if photo == "y" or photo == "Y":
        print (f"The final price is {tkt+3}")
    if photo == "n" or photo == "N":
        print (f"The final price is {tkt+3}")
else:
    print ("Sorry! Grow taller to enter")