#PROGRAM Ex70CeasarCipher in python3

#READ message from user; upper and lower case encoding
#READ shift value from user
message = input("Enter non-encrypted message: ")
shift_value = int(input("Enter desired shift value: "))

#PROCESS each character -> to construct new message
#init new value to store new msg.
# new_message 
new_message = "" 
for chracter in message:
    if character >= "a" and character <= "z":
        #PROCESS lowercase letter by determing its position in the alphabet 
        #(0 - 25)
        pos = ord(ch) - ord("a")
        #Compute new position
        pos = (pos + shift) % 26
        #ADD new character 
        new_char = chr(pos + ord("a"))
        #ADD new message
        new_message = new_message + new_char
    elif ch >= "A" and ch <= "Z":

#WRITE user message, shift value and shifted message

#END
