#       PROJECT_04_random-password-generator
import random
num_alpha_upper= int (input ("How many uppercase alphabets do you want? \n"))
num_alpha_lower= int (input ("How many lowercase alphabets do you want? \n"))
num_spcl = int (input ("How many special characters do you want out of 5? \n"))
num_num = int (input ("How many numbers do you wanr? \n"))
values = [num_alpha_upper, num_alpha_lower, num_spcl, num_num]
lst_upperalpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lst_loweralpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lst_spcl = ['!', '@', '#', '$', '&']
lst_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_allin1 = [lst_upperalpha, lst_loweralpha, lst_spcl, lst_numbers]
lst_passcode = []
for i in range (0,4):
    lst_rough=(random.sample(list_allin1[i], values[i]))
    for k in lst_rough:
        lst_passcode.append(k)
random.shuffle(lst_passcode)
password = ""
for j in lst_passcode:
    password += j
print ("Your password is : "+password+" \n\n\n")

# OR WE CAN ALSO USE THE random.choice() function (but if we use this function, cases of repetition might occur but while using random.sample(), we do not get any repitions)

#HOW?

# if we want to extract 2 upper case alphabets and the number of upper case alphabets is stored in num and the upper case alphabets are stored in the list lst_upperalpha:

# for i in range(1, num+1):
#   password += random.choice(lst_upperalpha)
# *same for other values


# one more problem of this tipe of logic is that it will generate the password like ARYCCugdt$#@8083 which is easy target for hackers as the sequence of upper case, lower case, spcl
# characters and numbers appearing is known. So for easy level, this is acceptable, for for real use, 