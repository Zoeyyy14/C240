import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
BUFFER_SIZE=4096
IP_ADDRESS='127.0.0.1'
PORT=8080
SERVER=None

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
setup()