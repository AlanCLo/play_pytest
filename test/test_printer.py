import pytest

from module1.printer import Printer


@pytest.mark.set1
def test_print_num():
    Printer.print_num(1)


@pytest.mark.set2
def test_print():
    Printer.print_str('hello world')
