sent_message = 'Fala meu bom'

with open ('sent_message.txt', 'w') as file:
    file.write(sent_message)

with open ('sent_message.txt', 'r+') as file: # The r+ is used to indicate both reading and writing are allowed in the file
    # Read the sent message from the file
    original_message = file.read()

    # Move the cursor to the beginning of the file
    file.seek(0)

    unsent_message = 'This message has been unsent.'

    file.truncate(len(unsent_message))

    file.write(unsent_message)

print('The message sent: ', original_message)
print('The unsent message: ', unsent_message)