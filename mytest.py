import uuid

class TestException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self) -> str:
        return f"TestException({self.msg})"

def my_test(iterations):
    a = dict()
    for i in range(iterations):
        a[str(i)] = { "id": uuid.uuid4(), "value": i}
    for i in range(iterations):
        key = str(i)
        if key in a:
            item = a[key]
            if not item["value"] == i:
                raise TestException("value error")
        else:
            raise TestException("key missing")
    l = map(lambda x: (str(a[x]["id"]), a[x]["value"]), a.keys())
    filtered = filter(lambda x: x[1] > iterations/2, l)
    result = list(filtered)
    if not len(result) == (iterations/2 -1):
        raise TestException("Count error")
