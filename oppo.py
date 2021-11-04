import socket


class Oppo:
    def __init__(self, host, from_port, to_port):
        self.host = host
        self.from_port = from_port
        self.to_port = to_port


    def is_open(self, result, port):
        if result == 0:
            print(f"Port: {port} :: open")


    def scan(self):
        for port in range(int(self.from_port), int(self.to_port)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((self.host, port))
            self.is_open(result, port)
            sock.close()
