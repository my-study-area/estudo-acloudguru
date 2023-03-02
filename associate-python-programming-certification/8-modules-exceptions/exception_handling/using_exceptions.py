
import sys

if len(sys.argv) < 2:
    raise Exception('not enough arguments')

name = sys.argv[1]
print(f"Name is {name}")
