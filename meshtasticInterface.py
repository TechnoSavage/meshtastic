""" text """


import meshtastic
import meshtastic.serial_interface

def serialPort():
    """ text """
    port = input('Enter serial/COM port for LoRa device: ').upper()
    interface = meshtastic.serial_interface.SerialInterface(port)
    return(interface)

def sendMessage(interface):
    """ text """
    message = input('message: ')
    interface.sendText(message)

def localConfig(interface):
    ourNode = interface.getNode('^local')
    print(ourNode.localConfig)

def main():
    port = serialPort()
    while True:
        command = input('''Choose one of the following options:
                1 - Send a message to send to the mesh
                2 - Change COM port
                3 - Change group
                4 - Print local config
                5 - exit
                Enter selection number: ''')
        if command == '1':
            message = sendMessage(port)
        elif command == '2':
            port = serialPort()
        elif command == '3':
            pass
        elif command == '4':
            print(localConfig(port))
        elif command == '5':
            exit()
        try:
            command = int(command)
        except ValueError as reason:
            print("That is not a valid selection.", reason)
        execute = {1: sendMessage,
                   2: serialPort,
                   3: '',
                   4: localConfig,
                   5: exit}
        if command in execute:
            try:
                option = execute[command]
                run = option()
                print(run)
            except KeyError as reason:
                print(reason)
        else:
            print("That is not a valid selection.")

if __name__ == "__main__":
    main()