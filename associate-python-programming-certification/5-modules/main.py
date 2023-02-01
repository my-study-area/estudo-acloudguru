print("We're import 'helpers' from 'main'")
from helpers import *
import extras

print(f'main = {__name__}')
name = "Keith Thompson"
print(f"Lowercase Letters: {extract_lower(name)}")
print(f"Uppercase Letters: {extract_upper(name)}")
