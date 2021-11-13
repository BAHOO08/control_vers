from socket import *


class Server:
    def __init__(self) -> None:
        self.ip = 'localhost'
        self.port = 3000
        self.buff_size = 1024
        self.tcp_ser_sock = socket(AF_INET, SOCK_STREAM)
        self.max_listen_val = 5


    def run(self) -> None:
        self.tcp_ser_sock.bind((self.ip, self.port))
        self.tcp_ser_sock.listen(self.max_listen_val)
        
        tcp_cli_sock, addr = self.tcp_ser_sock.accept()

        file_name = tcp_cli_sock.recv(self.buff_size).decode()
        print(file_name)
        f = open('server_files/' + file_name, 'wb')

        # временный бесконечный цикл
        while True:
            taked_data = tcp_cli_sock.recv(self.buff_size)

            if not taked_data:
                break

            f.write(taked_data)

        tcp_cli_sock.close()
        self.tcp_ser_sock.close()


if __name__ == '__main__':
    server = Server()
    server.run()
