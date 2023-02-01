from multiprocessing.spawn import _main
from unittest.main import MAIN_EXAMPLES
from pip import main

__all__ = ['extract_upper']

def extract_lower(phrase: str):
  return list(filter(str.isupper, phrase))

def extract_upper(phrase: str):
  return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print("HELLO FROM HELPERS")
