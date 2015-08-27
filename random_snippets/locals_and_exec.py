"""Why f1 function throws na exception but f2 works fine?"""
def f1():
    locals()["a"] = 1
    print(a)
    return

def f2():
    locals()["a"] = 1
    print(a)
    return
    exec ""
