"""module.py - an
example
of
a
Python
module
"""
import sys
#
__counter = 0


class Visitors:

    def __init__(self,n=0):
        self.__visit = n
    def get_num_visit (self):
        return self.__visit
    def __str__(self):
        return "Hello World !"
    def increment(self):
        self.__visit += 1






def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


def mysplit(s):
    maliste = []
    if len(s) == 0:
        return []
    else:
        chain = s.strip()
        mot = ''
        for i in range(len(chain)):
            if not chain[i].isspace():
                mot += chain[i]
                if i == len(chain) - 1:
                    maliste.append(mot)
            else:
                if mot != '':
                    maliste.append(mot)
                    mot = ''
    return maliste



if __name__ == "__main__":
    print("Don't run the program like this!")
    sys.exit()

