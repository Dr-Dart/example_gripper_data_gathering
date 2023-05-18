# -------------------------------------------------------------------------
# BSD 3-Clause License
# Copyright (c) 2023 Doosan Robotics
# All rights reserved.
# -------------------------------------------------------------------------
# Title: Robotiq gripper test client code using socket communication.
# Date: Apr, 20, 2023
# -------------------------------------------------------------------------
# Note, you need to run the DRL server code first in dart-studio and then run it.

# Import the python library.
import socket
import time
import datetime

# Define the host and port to connect to
HOST = '192.168.137.100'    # Replace with the server's hostname or IP address
PORT = 20002                # Replace with the server's port number

# Create a socket object and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Create a new file to save the received data
date_format = "%Y%m%d_%H%M%S'"
current_date = datetime.datetime.now()
formatted_date = current_date.strftime(date_format)[:-3]

# It performs socket communication with the server and saves the state data of the gripper.
filename = "sample_data_" + formatted_date + ".txt"
with open(filename, 'w') as f:

    # Sets the header of the file.
    file_header = "time, state, current\n"
    f.write(file_header)

    # Receive data from the server line by line and save it to the file
    while True:
        data = client_socket.recv(1024).decode()
        if not data:  # If the server has no more data to send, break the loop
            break
        if data.strip() == 'q':  # If the received data is 'q', exit the program
            print("Exiting program...")
            break
        # Save the received data.
        f.write(data)
        print(data)

# Close the socket and file
client_socket.close()
