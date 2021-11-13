from  socket import *

ip = "localhost"
port = 3000
buff_size = 1024

tcp_ser_sock = socket(AF_INET, SOCK_STREAM)
tcp_ser_sock.bind((ip,port))
tcp_ser_sock.listen(5)

tcp_cli_sock, addr = tcp_ser_sock.accept()

file_name = tcp_cli_sock.recv(buff_size).decode()
print(file_name)
f = open('server_files/' + file_name, 'wb')

while True:
    taked_data = tcp_cli_sock.recv(buff_size)

    if not taked_data:
        break

    f.write(taked_data)


tcp_cli_sock.close()
tcp_ser_sock.close()