import socket
from _thread import start_new_thread

class Server:
    def __init__(self) -> None:
        self.ip = 'localhost'
        self.port = 3000
        self.buff_size = 1024
        self.tcp_ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.max_listen_val = 5

    def sock_thread(self, socket):
        file_name = socket.recv(self.buff_size).decode()
        print(file_name)
        f = open('server_files/' + file_name, 'wb')
        while True:
            taked_data = socket.recv(self.buff_size)

            if not taked_data:
                break

            f.write(taked_data)
        socket.close()
    
    def run(self) -> None:
        self.tcp_ser_sock.bind((self.ip, self.port))
        self.tcp_ser_sock.listen(self.max_listen_val)

        while True:
            tcp_cli_sock, addr = self.tcp_ser_sock.accept()
            print(f"{addr} has connected")
            start_new_thread(self.sock_thread, (tcp_cli_sock,))

        
        self.tcp_ser_sock.close()


if __name__ == '__main__':
    server = Server()
    server.run()
