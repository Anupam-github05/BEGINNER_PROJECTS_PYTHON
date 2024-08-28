#PROJECT_03
#in this project we are going to simply devisew a game of rock pappers and scossors
import random
rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
response = 'Y'
while response == 'Y' or response == 'y':
    comp = random.choice([rock, paper, scissor])
    choice = int (input ("What do you choose? press 0 for rock, 1 for paper and 2 for scissors \n"))
    if choice == 0:
        print ("You chose: \n"+ rock)
        print ("Computer chose : \n"+comp)
        if comp == rock:
            print ("Tie \n")
        if comp == paper:
            print ("Compute Wins! Fatality! \n")
        if comp == scissor :
            print ("You Win! Victory! \n")
    if choice == 1:
        print ("You chose: \n"+ paper)
        print ("Computer chose : \n"+comp)
        if comp == rock:
            print ("You Win! Victory! \n")
        if comp == paper:
            print ("Tie \n")
        if comp == scissor :
            print ("Compute Wins! Fatality! \n")
    if choice == 2:
        print ("You chose: \n"+ scissor)
        print ("Computer chose : \n"+comp)
        if comp == rock:
            print ("Compute Wins! Fatality! \n")
        if comp == paper:
            print ("You Win! Victory! \n")
        if comp == scissor :
            print ("Tie \n")
    if choice !=0 and choice !=1 and choice !=2:
        print ("Wrong Input!")
    response =" "
    while (response != 'Y' and response != 'y') and (response != 'n' and response != 'N'):
        response = input ("Do you want to continue? Press y for yes and n for no \n")
        if (response != 'Y' and response != 'y') and (response != 'n' and response != 'N'):
            print ("Wrong input! Try again! ")