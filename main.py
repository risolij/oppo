from oppo import Oppo
import pyfiglet
import sys
import time
import colorama
from colorama import Fore,Back



def timeit(func):
    def wrapper():
        time_start = time.time()
        func()
        time_end = time.time()
        print(f"Function {__name__}:: Took {round(time_end - time_start, 4)} seconds")
    return wrapper


def banner(func):
    def wrapper():
        print(Fore.GREEN + pyfiglet.figlet_format("(Op)en (po)rts") + Fore.RESET)
        print(Fore.CYAN + "⎽" * 60 + Fore.RESET)
        func()
        print(Fore.CYAN + "⎺" * 60 + Fore.RESET)
    return wrapper


def usage():
    print("You need at least 3 items passed to the script")
    print("./main.py <host> <from_port> <to_port>")
    exit()


def is_three_args():
    if len(sys.argv) != 4:
        usage()


@timeit
@banner
def main():
    is_three_args()
    oppo = Oppo(sys.argv[1], sys.argv[2], sys.argv[3]);
    oppo.scan()


if __name__ == "__main__":
    main()
