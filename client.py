from socket import *


class Client:
    def __init__(self) -> None:
        self.ip = '192.168.0.182'
        self.port = 3000
        self.buff_size = 1024
        self.tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
    

    def run(self) -> None:
        while True:
            cmd = input('Get command: ')

            if cmd == 'sf':
                file_name = input('Enter file name: ')
                self.send_file(file_name)
            elif cmd == 'close':
                break

        self.tcp_cli_sock.close()


    def connect_port(self) -> None:
        self.tcp_cli_sock.connect((self.ip, self.port))


    def send_file(self, file_name: str):
        self.tcp_cli_sock.send(file_name.encode())
        f = open('client_files/' + file_name, 'rb')
        send_data = ''
        while send_data != b'':
            send_data = f.read(self.buff_size)
            self.tcp_cli_sock.send(send_data)


if __name__ == '__main__':
    client = Client()
    client.connect_port()
    client.run()
