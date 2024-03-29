# import sys

# from .errors import ArgumentError

# def main():
#     if len(sys.argv) < 2:
#         raise ArgumentError('too few arguments')
#     print(f"Name is {sys.argv[1]}")

import sys

from .errors import ArgumentError

def main():
    # if len(sys.argv) < 2:
    #     raise ArgumentError("too few arguments")
    assert len(sys.argv) >= 2, "too few arguments"
    print(f"Name is {sys.argv[1]}")
