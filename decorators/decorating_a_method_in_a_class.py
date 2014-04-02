import sys

try:
    import hukka
except ImportError:
    def deco(f):
        def new_func(self, params="world"):
            f(self, params)
        return new_func

class A:
    @deco
    def a(self, pa):
        print "hello %s" % pa

print "run 1"
A().a()
print "run 2"
A().a("world!")
