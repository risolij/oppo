from oppo import Oppo
from lib import *


@timeit
@banner
def main():
    oppo = Oppo(sys.argv[1], sys.argv[2], sys.argv[3]);
    oppo.scan()


if __name__ == "__main__":
    is_three_args()
    main()
