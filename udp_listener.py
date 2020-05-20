from tcp_client import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.settimeout(5)

server_address = ('255.255.255.255', 9434)
message = 'pfg_ip_broadcast_cl'


def listener():
    try:
        while True:
            print('sending: ' + message)
            sent = sock.sendto(message.encode(), server_address)

            print('waiting to receive')
            data, server = sock.recvfrom(4096)
            if 'pfg_ip_response_serv' in data.decode('UTF-8'):
                print('Received confirmation')
                print('Server ip: ' + str(server[0]))
                print('Server port: ' + str(server[1]))
                print('Client port: ' + str(int(data[21:])))
                client(int(data[21:]))
                break

            else:
                print('Verification failed')

            print('Trying again...')
    finally:
        sock.close()

# listener()
