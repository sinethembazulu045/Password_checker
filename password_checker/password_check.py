import re
class Password_Checker:

    def __init__(self, password):
        self.password = str(password)
        pass

    def lowercase(self, password):
        return any(char.islower() for char in password)

    def uppercase(self,password):
        UPPERCASE = any(char.isupper() for char in password)
        return UPPERCASE

    def special_charectors(self,password):
        SpecialSym =['$', '@', '#', '%'] 
        SPECIALSYM =any(char in SpecialSym for char in password)
        return SPECIALSYM
    
    def num_digits(self,password):
        NUM_DIGITS =any(char.isdigit() for char in password)
        return NUM_DIGITS

    def password_is_ok(self,password):
        passed_conditions = 0
        if len(password)==0:
            return False
        passed_conditions +=1

        if len(password) <= 8:
            return False
        passed_conditions += 1

        if self.num_digits(password) == True:
            passed_conditions += 1

        if self.lowercase(password) == True:
            passed_conditions += 1

        if self.uppercase(password) == True:
            passed_conditions += 1

        if self.special_charectors(password)== True:
            passed_conditions += 1
        # return passed_conditions >= 3
        if passed_conditions >= 3:
            return True
        else:
            return False
    def password_is_valid(self,password): 
        
        SpecialSym =['$', '@', '#', '%'] 
        val = True
        if len(password)==0:
            raise Exception("password should exist")
        
        if len(password) < 8: 
            raise Exception('length of the password should be more than 8') 
            val = False
            
        if not any(char.isdigit() for char in password): 
            raise Exception('Password should have at least one numeral') 
            val = False
            
        if not any(char.isupper() for char in password): 
            raise Exception('Password should have at least one uppercase letter') 
            val = False
            
        if not any(char.islower() for char in password): 
            raise Exception('Password should have at least one lowercase letter') 
            val = False
            
        if not any(char in SpecialSym for char in password): 
            raise Exception('Password should have at least one of the symbols $@#') 
            val = False
        if val: 
            return val 
     #def password_is_ok(self,password_is_ok):
      #  password_conditions = [len(password)>8,]
       # for i in password_conditions:
           # if i >=3:      
       # return print(password_is_ok)
    
    #def password_check(self, password):
        #pass




  
# Driver Code         
if __name__ == '__main__': 
    password ="qwLd"
    password_check = Password_Checker(password)
    if (password_check.password_is_ok(password)==True):
        print("password is ok")
  
    else:
        print("Password is not okay") 

    if (password_check.password_is_valid(password)==True):
        print("password is valid")
    else:
        print("password is invalid")