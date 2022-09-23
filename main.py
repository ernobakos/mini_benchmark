import timeit

import_module = "import mytest"

testcode = '''
iterations = 200
mytest.my_test(iterations)
'''
if __name__ == "__main__":
    print("Time taken:" , timeit.timeit(stmt = testcode, setup=import_module, number = 1000))
