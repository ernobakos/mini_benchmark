from datetime import datetime
import mytest

import multiprocessing as mp

def chunkify(lst,n):
    return [lst[i::n] for i in range(n)]

def testmp(cpus, total, iterations):
    pool = mp.Pool(cpus)

    ranges = chunkify(range(total), cpus)
    r = map(lambda x : (x,iterations), ranges)
    params = list(r)
    st = datetime.now()
    pool.starmap(mytest.my_testmp,params)
    dur = datetime.now() - st
    pool.close()
    result = pool.join()
    return dur.total_seconds()