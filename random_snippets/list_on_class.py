# coding: utf-8


class Cls(object):
    events = []

instance = Cls()
instance.events.append(1)

print(instance.events)      # => [1]
print(Cls.events)           # => [1]

instance.events = []
print(instance.events)      # => []
print(Cls.events)           # => [1]

instance.events.append(2)
print(instance.events)      # => [2]
print(Cls.events)           # => [1]

instance = Cls()
instance.events.append(3)
print(instance.events)      # => [1, 3]
print(Cls.events)           # => [1, 3]

instance.events[:] = []
print(instance.events)      # => []
print(Cls.events)           # => []
