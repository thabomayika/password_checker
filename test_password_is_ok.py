import pytest
import re
from password_checker import password_is_ok
def test_password_is_ok():
        """test that exception is raised for invalid passwords"""
        with pytest.raises(Exception) as error:
                assert None == password_is_ok('pppppppp') 
        assert str(error.value) == 'password should atleast have one digit' 

        
        with pytest.raises(Exception) as error:
                assert password_is_ok('') == Exception() 
        assert str(error.value) == 'password should atleast have one lowercase'
        
        """test that valid passwords work"""
        assert password_is_ok('') == True
        assert password_is_ok('longroo') == True
        assert password_is_ok('L8PORJECT') == True
        assert password_is_ok('Long8root@') == True
