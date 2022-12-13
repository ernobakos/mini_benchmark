import sys

total = 1000
iterations = 200

def test1():
    import uptest
    print("1 Thread: Time taken:" , uptest.testup(total,iterations))

def test2():
    import mptest
    import multiprocessing as mp
    cpus = mp.cpu_count()
    print("{} Thread: Time taken:".format(cpus) , mptest.testmp(cpus, total, iterations))

if __name__ == "__main__":
    print(f"Using python:{sys.version}")
    test1()
    test2()
