
def get_fullname (first_name, last_name, middle_name = ''):
    print(bool(middle_name))
    if middle_name == '':
        return f"{first_name} {last_name}"
    else:
        return f"{first_name} {middle_name} {last_name}" # Order of words is here

print (get_fullname("Andy", "Stefanenko", ""))
    
        
    
        