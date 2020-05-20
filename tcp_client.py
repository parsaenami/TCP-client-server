from socket import *


def client(port_in):
    # port = 65432
    port = port_in
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((gethostname(), port))

        username = input('username: ')
        while True:
            st = username + ' > '
            msg = input(st)
            if msg == 'terminate':
                break

            s.send((username + '/$/' + msg).encode())

            data = s.recv(1024).decode()
            try:
                print(data.split('/$/')[0] + '> ' + data.split('/$/')[1])
            except:
                break
