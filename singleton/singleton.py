class DBConn:
    h = {}

    @classmethod
    def get_db_conn(cls, p):
        try:
            cls.h[p]
        except KeyError:
            cls.h[p] = SomeClass(p)

        return cls.h[p]

class SomeClass:
    def __init__(self, a):
        self.a = a

    def pp(self):
        print "Inside A, value of a: %d" % self.a

s1 = DBConn.get_db_conn(1)
s2 = DBConn.get_db_conn(2)

s2.pp()
s1.pp()
s2.pp()
