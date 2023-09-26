message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for char in message:
    if 'a'<= char <= 'z':
        value = ord('a')
    elif 'A' <= char <= 'Z':
        value = ord('A')
    else:
         value = 0
        
    if  value != 0:
        var = ord(char) - value
        var = (var + offset) % 26
        new_char = chr(var + value)
    
    else:
        new_char = char
    
    encoded_message += new_char

    print(encoded_message)
