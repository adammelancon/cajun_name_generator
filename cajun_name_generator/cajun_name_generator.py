"""Main module."""
import random
from cajunnamelist import lastnames, firstnames

class CajunNames():
    '''random_last_name() gives random last name
       random_first_name() gives random first name
       random_full_name() gives a random first name
    '''
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
