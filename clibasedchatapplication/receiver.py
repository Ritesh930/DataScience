import socket
try:
    # Creating socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # dgram--data gram
    print("Socket created successfully")
    ## sender k aandar address hamesha receiver ka hi aata hai
    
    ip_add = "192.168.121.4"  # IP address to bind to
    port = 8888  # Port number to bind to (from 0 to 65535)
    complete_add = (ip_add, port)  # Complete address to bind to
    s.bind(complete_add)  # Binding the socket to the address

    while True:
        message, sender_address = s.recvfrom(1024)  # Receiving message from the socket

        print("Raw Message:", message)  # Displaying the raw message
        print("Sender Address:", sender_address)  # Displaying the sender's address
        decoded_message = message.decode("ascii")
        print("message",decoded_message)  # Decoding and displaying the message
except socket.error as e:
    print("An error occurred:", e)        