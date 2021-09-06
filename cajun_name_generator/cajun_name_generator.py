"""Main module."""
import random
from cajunnamelist import lastnames, firstnames

class CajunNames():
    def __init__(self) -> None:
        self.lastnames = lastnames
        self.firstnames = firstnames
    
    def random_last_name(self):
        return random.choice(self.lastnames)

    def random_first_name(self):
        return random.choice(self.firstnames)

    def random_full_name(self, count=1):
        fullname = random.choice(self.firstnames) + " " + random.choice(self.lastnames)
        return fullname
