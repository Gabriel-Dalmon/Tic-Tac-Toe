import socket
import pickle


class Socket:
    def __init__(self, host = "localhost"):
        self.HOST = host
        self.PORT = 47054
        self.HEADERLENGTH = 8
        self.connectServer()       

    def connectServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))
        return self.socket


    def recvMsg(self):
        data = self.socket.recv(self.HEADERLENGTH)
        dataLength = int(data)
        data = self.socket.recv(dataLength)
        data = pickle.loads(data)
        return data

    def sendMsg(self, data):
        data = pickle.dumps(data)
        data = bytes(f'{len(data):<{self.HEADERLENGTH}}', "utf-8") + data
        self.socket.send(data)


if __name__ == "__main__":
    socket = Socket()