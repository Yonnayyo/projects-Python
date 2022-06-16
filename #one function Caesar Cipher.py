#one function
logo = """           
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
"""
print(logo)

alfabet_prim=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alfabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    def caesar():
        direction=input("Type 'encode' or 'decode': \n")
        text=input("Type your message here: \n").lower()
        shift=int(input("Type the shift nr: \n"))
        shift%=len(alfabet_prim)
        if direction == "encode":
            cipher_text=""
            plain_text=text
            for letter in plain_text:
                if letter not in alfabet_prim:
                    cipher_text+=letter
                else:
                    position=alfabet.index(letter)
                    new_position=position+shift
                    cipher_text += alfabet[new_position]
            print(f"The encoded text is: {cipher_text}")
        elif direction == "decode":
            plain_text=""
            cipher_text=text
            for letter in cipher_text:
                position=alfabet.index(letter)
                new_position=position-shift
                plain_text += alfabet[new_position]
            print(f"The decoded text is: {plain_text}")
    caesar()
    answer=input("Do you want to run again? Type yes or no here: ").lower()
    if answer=="yes":
        caesar()
        continue
    else:
        print("Goodbye")
        break
