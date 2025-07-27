
import socket
import time

# Server details
HOST = '127.0.0.1'
PORT = 6001

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET specifies the address family (IPv4), and SOCK_STREAM specifies the socket type (TCP).

# Connect to the server
client_socket.connect((HOST, PORT))

# Main loop for client interaction (infinite loop for the client to continuously interact with the server)

while True:
    # Prompt the user to enter a message in a specific format
    print("\nEnter Proxy Message in the form of")
    print("OP=XXX;IND=Ind1,Ind2,..;DATA=Dat1,Dat2...;")
    
    # Get user input for the message
    message = input("Enter Message: ")

    # Send the message to the server after encoding it into bytes using UTF-8
    client_socket.sendall(bytes(message, 'utf-8'))
    
    # Pause for 0.5 seconds
    time.sleep(0.5)

    # Receive the response from the server
    dataReceived = client_socket.recv(1024) #1024  bytes
    
    # Decode the received data into a string
    dataReceived = dataReceived.decode('utf-8')

    # Display the received message
    print("\nReceived Message is:")
    print(dataReceived, "\n\n")

    #The loop then repeats, allowing the client to send and receive messages in an interactive manner with the server.




