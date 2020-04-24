#!/usr/bin/env python

from module1.adder import Adder
from module1.printer import Printer


def main():
    small_num = Adder.add_num(10, 20)
    Printer.print_num(small_num)

    big_str = Adder.add_str("This ", "is a big string")
    Printer.print_str(big_str)


if __name__ == "__main__":
    main()
