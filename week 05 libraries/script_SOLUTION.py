'''
Script imports the password_checker module. When it runs, it asks the user for a password and print the strength score,
along with some context to explain if the password is strong enough. 
'''
from password_checker_SOLUTION import password_strength

strong_password = False

#Loop continuously until a strong password is created
while strong_password == False: 
    pw = input("Enter a new password. ")
    
    #call the password strength function from the imported module and store the strength returned into the score variable
    score = password_strength(pw)
    
    if score < 3:
        print (f" Password score = {score}. Password not strong enough, try again.")
    elif score in (3,4): 
        strong_password = True
        print (f"Password score = {score}. Your password has been accepted. ")
    else: 
        strong_password = True
        print(f"Password score =  {score}. Your password is very strong!" )
