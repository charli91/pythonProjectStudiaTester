class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    a = 1
    print(Bcolors.HEADER, a, "HEADER")
    print(Bcolors.OKBLUE, a + 1, " OKBLUE")
    print(Bcolors.OKCYAN, a + 2, " OKCYAN")
    print(Bcolors.OKGREEN, a + 3, " OKGREEN")
    print(Bcolors.WARNING, a + 4, " WARNING")
    print(Bcolors.FAIL, a + 5, " FAIL")
    print(Bcolors.ENDC, a + 6, " ENDC")
    print(Bcolors.BOLD, a + 7, " BOLD")
    print(Bcolors.UNDERLINE, a + 8, " UNDERLINE")


if __name__ == '__main__':
    main()
