#import re
import pytest
from password_checker import *
def test_password_is_valid():
     
#test that exception is raised for invalid passwords

        with pytest.raises(Exception):
                assert password_is_valid('') == "password should exist"
                # assert password_is_valid('TTTTTTTTT') == 'password should have atleast one lowercase letter'
                # assert password_is_valid('ttttttttt') == 'password should atleast have one uppercase letter'
                # assert password_is_valid('tTttttttt') == 'password should atleast have one digit'
                # assert password_is_valid('tVp9rart') == 'password should be longer than than 8 characters'
        
        
        
        
        
        
        
                
       