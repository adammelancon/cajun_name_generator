import random
from cajun_name_generator.cajunnamelist import lastnames, firstnames


class Cajunnames():
    '''random_last_name() gives random last name
       random_first_name() gives random first name
       random_full_name() gives a random first name
    '''
    def __init__(self) -> None:
        self.lastnames = lastnames
        self.firstnames = firstnames
    
    def random_last_name(self, count=1):
        names = []
        for _ in range(0,count):
            lasts = random.choice(self.lastnames)
            names.append(lasts)
        print(names)
        return(names)

    def random_first_name(self, count=1):
        names = []
        for _ in range(0,count):
            firsts = random.choice(self.firstnames)
            names.append(firsts)
        print(names)
        return(names)

    def random_full_name(self, count=1):
        names = []
        for _ in range(0,count):
            fullname = random.choice(self.firstnames) + " " + random.choice(self.lastnames)
            names.append(fullname)
        print(names)
        return names
