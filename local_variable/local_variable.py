def dekor(timeout=None):
    def _fun_dekor(fn):
        def _inner(*args, **kwargs):
            print(timeout)
            val = fn(*args, **kwargs)
            timeout = None  # Dlaczego ta linia powoduje taki problem?
            return val
        return _inner
    return _fun_dekor


@dekor(timeout=300)
def test(a, b):
    print("a+b=%s" % (a + b))

test(1, 2)
