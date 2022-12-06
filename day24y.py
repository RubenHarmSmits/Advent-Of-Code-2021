import threading


def printName(name):
    for _ in range(9999):
        print(name)

a = threading.Thread(printName('Ruben'))
b = threading.Thread(printName('Irene'))


a.start
b.start

a.join
b.join


