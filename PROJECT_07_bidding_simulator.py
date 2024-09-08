#PROJECT_07_bidding_simulator
import os                               #(to know about the operating syatem i'm working on)
name_dict = {}
def bid_check (dict):                   #checking who has got the highest bid!
    max = 0
    win =[]
    name_of_winner = ""
    for key in dict:
        if dict[key] >= max:
            max = dict[key]
            name_of_winner = key
    win = [name_of_winner, max]
    return win

def clear_screen():                     #a user defined function to clear the contents of the terminal window whenever the function is called
    if os.name == "nt":
        os.system("cls")
    else:
         os.system("clear")
clear_screen()

more_mem = True
while more_mem == True:
    print ("Welcome to secret auction program! Here we do anonymous bidding! ")
    print (r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
        '''
    )
    name= input ("What is your name? \n")
    bid = float(input ("What's your bid? \n$"))
    name_dict[name] = bid
    cond = True
    while cond == True:    
        choice = input ("\n\n Are there any other bidders? type 'Yes' or 'No' \n").lower()
        if choice.isalpha():
            if choice == 'yes':
                more_mem = True
                cond = False
                clear_screen()
            elif choice == 'no':
                more_mem = False
                cond = False
                clear_screen()
            else:
                print ("\n\n Wrong input! Try again! \n\n")
                cond = True
winner = bid_check(name_dict)
print (f"\n\n\nThe winner is {winner[0]} with a bid of ${winner[1]} \n\n\n")