import sys

try:
    import hukka
except ImportError:
    def deco(f):
        def new_func(self, params):
            print params
            f(self, params)
        return new_func

class A:
    @deco
    def a(self, pa):
        print "hello %s" % pa


A().a("world!")
