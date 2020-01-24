import re
def password_is_valid(password):

     ############# password should exist ################

    if len(password) != 0:
        print("password exist")
    else:
        raise Exception("password should exist")
    
    
     ############# length of password is long enough #######
    
    if len(password) > 8:
        print("Valid length")
    else:
        raise Exception('password should be longer than than 8 characters')

     ############## lowercase characters ###############
    
    if (any(c.islower() for c in password)):
        print("Valid atleast one lowercase letter")
    else:
        raise Exception("password should have at least one lowercase letter")

     ############### Uppercase characters ############### 
                 
    if (any(c.isupper() for c in password)):
        print("Valid atleast one uppercase letter")
    else:
        raise Exception("password should have at least one uppercase letter")   

     ################## Digits ################ 

    if re.search('[0-9]',password):
        print("valid number of Digits")
    else:
        raise Exception('password should at least have one digit')

     ################ special characters ################
    
    if re.search(r"[!@#$%^&*(),.?:{}|<>]", password):
        print("valid number of special characters")
    else:
        raise Exception('password should have at least one special character')

#password_is_valid("")

################ fuction that callings the 3 arguments ###################

def password_is_ok(password):
    count = 0
    if (password != 0):
        if len(password) > 8:
            if (any(c.islower() for c in password)) or re.search(r"[!@#$%^&*(),.?:{}|<>]", password) or (any(c.isupper() for c in password)) or re.search(r"[!@#$%^&*(),.?:{}|<>]", password):
                count += 1                              
                    

            else:
                pass
        else:
            raise Exception('Password is never Ok if less than 8 characters')
    else:
        raise Exception('Password is never Ok if does not exist')


    if count ==1:
        return True    
##password_is_ok('')

