from socket import *


def server(port_in):
    # port = 65432
    port = port_in
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((gethostname(), port))
        s.listen(4)
        conn, addr = s.accept()
        username = input('username: ')

        with conn:
            print('connected with', addr)

            while True:
                data = conn.recv(1024).decode()
                if data == 'terminate':
                    break

                try:
                    print(data.split('/$/')[0] + ' > ' + data.split('/$/')[1])
                except:
                    exit(1)

                st = username + ' > '
                msg = input(st)
                if msg == 'terminate':
                    exit(1)

                conn.send((username + '/$/' + msg).encode())
