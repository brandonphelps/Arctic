
from test import add
from datetime import datetime
import time

if __name__ == "__main__":
    start = datetime.now()
    t = []
    for i in range(1000):
        t.append(add.delay(i, i))
    
    done = False
    count = len(t) - 1
    while not done:
        print "Running", (datetime.now() - start)
        done = True
        if not t[count].ready():
            done = False
    end = datetime.now()

    print "Total time", (end - start)
