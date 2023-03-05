
# import sys

# if len(sys.argv) < 2:
#     raise Exception('not enough arguments')

# name = sys.argv[1]
# print(f"Name is {name}")

# import sys

# from cli import main
# from cli.errors import ArgumentError

# try:
#     main()
# except ArgumentError as err:
#     print(f"Error: {err}")
#     sys.exit(1)

import sys

from cli import main
from cli.errors import ArgumentError

try:
    main()
except (ArgumentError, AssertionError) as err:
    print(f"Error: {err}")
    sys.exit(1)
