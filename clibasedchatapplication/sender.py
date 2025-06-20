import socket
try:
    ##creating socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #dgram--data gram
    print("Socket created successfully")
    ip_add ="192.168.121.4"
    port = 8888     #from 0 to 65535
    target_add = (ip_add, port)  #target address
    message = input("Enter the message to send: 😎")  #message to send
    encoded_message = message.encode()  #encoding the message

    s.sendto(encoded_message, target_add)  #sending the message
    print("Message sent successfully! ")
    s.close()  #closing the socket


except socket.error as e:
    print("An error occurred:", e)  #error message 