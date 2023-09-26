message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""


for ch in message:
    if ch.isalpha():
        new_ch = ord(ch) + offset
        if new_ch > ord('z'):
            new_ch -= 26
        elif new_ch < ord('a'):
            new_ch += 26
        encoded_message += chr(new_ch)
    else:
        encoded_message += ch

print (encoded_message)