import socket
import pickle


class Socket:
    def __init__(self):
        self.HOST = ''
        self.PORT = 47054  
        self.HEADERLENGTH = 8
        self.socketsList = []
        self.connectSockets()

    def connectSockets(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.bind((self.HOST, self.PORT))
            self.s.listen(2)
            while len(self.socketsList)<2:
                conn, addr = self.s.accept()
                self.socketsList.append((conn,addr))
            print("Connected to : ", self.socketsList)

    def recvMsg(self, clientSocket):
        print("receive :")
        data = clientSocket.recv(self.HEADERLENGTH)
        dataLength = int(data)
        data = clientSocket.recv(dataLength)
        data = pickle.loads(data)
        return data

    def sendMsg(self, clientSocket, data):
        data = pickle.dumps(data)
        data = bytes(f'{len(data):<{self.HEADERLENGTH}}') + data
        clientSocket.send(data)

if __name__ == "__main__":
    socket = Socket()