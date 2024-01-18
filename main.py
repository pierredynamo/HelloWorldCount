# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from module import Visitors

if __name__ == '__main__':
    c = 0
    try:
        stream = open('number.txt', 'r+')
        valour = stream.read()
        if valour != '' and valour.isalnum():
            if int(valour) >= 1:
                c = int(valour)
            else:
                c = 0
        visitor = Visitors(c)
        visitor.increment()
        print(visitor.get_num_visit())
        print(visitor, " This program was already executed " + str(visitor.get_num_visit()), end="")
        print(" number of times.", end="")
        stream.seek(0)
        stream.write(str(visitor.get_num_visit()))
        stream.close()
    except Exception as e:
        print(e)
    finally:
        print("\nThanks for your time.")
