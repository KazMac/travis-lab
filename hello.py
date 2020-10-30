def inputUserChoice():
    name = input("Enter name: ")
    return name


def createMessage(name_msg):
    message_created = "Hello " + name_msg
    return message_created


def printMessage(output_message):
    print(output_message)

name = inputUserChoice()
message = createMessage(name)
printMessage(message)
