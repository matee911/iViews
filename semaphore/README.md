Implement in python distributed semaphore.
Interface should be the same as in built-in semaphore (
http://docs.python.org/2/library/threading.html#semaphore-objects), 
but it must works in distributed environment (many threads on many servers).

```
pip install -r requirements.txt
python master.py # to start master node
python thread.py # to start worker
```

TODO
====

Configurable master node IP address :)

