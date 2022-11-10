from datetime import datetime
import mytest

def testup(total, iterations):
    st = datetime.now()
    for x in range(total):
        mytest.my_test(iterations)
    dur = datetime.now() - st
    return dur.total_seconds()
