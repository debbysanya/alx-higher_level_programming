#!/usr/bin/python3
def add_arg(argv):
    size = len(argv) - 1
    if size == 0:
        print("{:d}".format(size))
        return
    else:
        i = 1
        add = 0
        while i <= size:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)

