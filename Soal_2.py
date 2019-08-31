import re

input = str(input("Masukan Username : "))
def is_username_valid(input):
    if len(input) > 9 :
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$",username) != None:
            return False
            
    if is_username_valid("lima5") == True:
        print("True")
    else:
        print("False")

is_username_valid(input)