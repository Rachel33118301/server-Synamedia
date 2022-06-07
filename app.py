#!/usr/bin/python

import os
from socket import *
import select
import hashlib
import json
from datetime import datetime


# Assigning server IP and server port
serverName = "0.0.0.0"
serverPort = 5000
# Setting timeout
timeout = 3
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
# While loop for the receiving of file
while True:
    data, serverAddress = serverSocket.recvfrom(1024)
    if data:
        decoded_data = json.loads(data.decode())
        md5_returned = hashlib.md5((decoded_data['file']).encode()).hexdigest()

        if json.loads(data.decode())['hash'] == md5_returned:
            print("MD5 verified OK.")
        else:
            print("MD5 verification failed!.")

        path = f'.\\recived_files'
        os.makedirs(path, exist_ok=True)
        file_name = f'{decoded_data["name"]}_{datetime.now().strftime("%H_%M_%S")}'

        f = open(f"{path}\\{file_name}.txt", "w")
        f.write(decoded_data['file'])
        f.close()

        print(f"File h8 been Received, located in {path}")
