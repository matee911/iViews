# coding: utf-8


class Foo(object):
    events = []

foo = Foo()
foo.events.append(1)

print foo.events    # => [1]
print Foo.events    # => [1]

foo.events = []
print foo.events    # => []
print Foo.events    # => [1]
