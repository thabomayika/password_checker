import re
def password_is_valid(password):
     ## password should exist
    if (password != None):
        print("password exist")
    else:
        raise Exception("password should exist")
    
    
     ## length of password is long enough
    
    if len(password) > 8:
        print("Valid length")
    else:
        raise Exception('password should be longer than than 8 characters')

     ## lowercase characters
    
    character = r'[a-z]'

    for c in character:
        if c != character: 
            print("Valid atleast one lowercase letter")
        else:
            raise Exception("password should have at least one lowercase letter")

     ## Uppercase characters 
     
    characters = r'[A-Z]'             
    for i in characters: 
        if i != characters:
            print("Valid atleast one uppercase letter")
        else:
            raise Exception("password should have at least one uppercase letter") 

     # Digits 

    if re.search('[0-9]',password):
        print("valid number of Digits")
    else:
        raise Exception('password should at least have one digit')

     #special characters
    
     # special = r"[+]"
     # for s in special:
    if re.search(r"[+]",password):
        print("valid number of special characters")
    else:
        raise Exception('password should have at least one special character')



## fuction that callings the 3 arguments
def password_is_ok(password):
    count = 0
    if (password != None):
        count += 1
        if len(password) > 8:
            count += 1
            characters = r'[A-Z]'
            if characters:
                count += 1                              


    if count > 3:
        return True
    else:
        return False

    ### never ok statement
    count = 0
    if (password == 0):
        count += 1
        if len(password) > 8:
            count += 1
        
    if count < 2:
        print("password is never Ok")        
password_is_ok('jhfgdhsjaibr2?+')

