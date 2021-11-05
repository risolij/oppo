import socket
import colorama
from colorama import Fore


GREEN = Fore.GREEN
RESET = Fore.RESET


class Oppo:

    def __init__(self, host, from_port, to_port):
        self.host = host
        self.from_port = from_port
        self.to_port = to_port


    def is_open(self, result, port):
        if result == 0:
            self.printout(port)


    def service_name(self, port):
        return socket.getservbyport(port)


    def create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        return sock


    def connect(self, sock, port):
        return sock.connect_ex((self.host, port))


    def close(self, sock):
        sock.close()


    def scan(self):
        for port in range(int(self.from_port), int(self.to_port)):
            try:
                sock = self.create_socket()
                result = self.connect(sock, port)
                self.is_open(result, port)
                self.close(sock)
            except Exception:
                print(f"Failed to connect")
                exit(1)


    def printout(self, port):
        print(f" ┠──────  {GREEN} 🔓 {RESET} {port} ⇀ {GREEN} open :: {self.service_name(port)} {RESET}")

