from multiprocessing.spawn import _main
from unittest.main import MAIN_EXAMPLES
from pip import main

__all__ = ['extract_upper']

def extract_lower(phrase: str):
  return list(filter(str.islower, phrase))

def extract_upper(phrase: str):
  """
  extract_upper takes a string and returns a list containing
  only the uppercase characters from the string

  >>> extract_upper("Hello There, BOB")
  ['H', 'T', 'B', 'O', 'B']
  """
  return list(filter(str.isupper, phrase))

if __name__ == "__main__":
    print("HELLO FROM HELPERS")
