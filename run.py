# Your code goes here.
from pprint import pprint
import time

def machineprint(text, delay = 0.1):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()