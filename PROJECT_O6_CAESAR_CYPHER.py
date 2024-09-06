#PROJECT_O6_caesar_cypher
#the program either encrypts or decrypts a message beased on the shift provided by the user. For example if shift is = 2 then a is printed as c , b as d...z as b and soo on
# during encryption and vice-versa during decryption.
#this project uses user defined function





print (r'''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''' )

def encryption (msg, shift):
    msg = msg.lower()
    encrypt_msg = ""
    nshift = 0
    if shift > 36:
        shift = shift%36
    for i in msg:
        if i.isalpha():
            if ord(i)+ shift <= 122:
                encrypt_msg += (chr(ord(i)+shift))
            if ord(i) + shift > 122:
                nshift = (ord(i) + shift) - 122
                encrypt_msg += (chr(97+(nshift-1 )))
        else:
            encrypt_msg += i
    print ("The encrypted message is "+encrypt_msg+ "\n\n\n")
def decryption(msg,shift):
    msg = msg.lower()
    decrypt_msg = ""
    nshift = 0
    if shift > 36:
        shift = shift%36
    for i in msg:
        if i.isalpha(): 
            if ord(i) - shift >= 97:
                decrypt_msg += (chr(ord(i)- shift))
            if ord(i) - shift < 97:
                nshift = 97 - (ord(i) - shift)
                decrypt_msg += (chr(122-(nshift-1 )))
        else:
            decrypt_msg += i
    print ("The encrypted message is "+decrypt_msg+ "\n\n\n\n")
opt = "0"
while opt == "0":
    choice = input ("Do you want to encode a message or decode a given message? press 'Encode' to encode a message and press 'Decode' to decode a message \n\n\n").lower()
    if choice == "encode":
        txt = input ("\n\nEnter message : \n")
        sh = int (input ("\n\nEnter shift : \n"))
        encryption (txt, sh)
    elif choice == "decode":
        txt = input ("\n\nEnter message : \n")
        sh = int (input ("\n\nEnter shift : \n"))
        decryption(txt, sh)
    else:
        print ("Sorry wrong input! ")
    opt = input ("\n\nEnter 0 to try again and any other key to exit \n\n")