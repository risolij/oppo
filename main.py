import sys
from oppo import Oppo
import time


def timeit(func):
    def wrapper():
        time_start = time.time()
        func()
        time_end = time.time()
        print(f"Function {__name__}:: Took {time_end} seconds")
    return wrapper


def banner(func):
    def wrapper():
        print("-" * 50)
        func()
        print("-" * 50)
    return wrapper


@timeit
@banner
def main():
    oppo = Oppo(sys.argv[1], sys.argv[2], sys.argv[3]);
    oppo.scan()


if __name__ == "__main__":
    main()
