from gevent import pywsgi
import gevent.monkey
gevent.monkey.patch_socket()
import urllib2
from gevent.queue import Queue
from gevent.event import Event

e = Event()
q = Queue()
count = 0
def fb_call(environ, start_response):
    global count, q
    start_response('200 OK', [('Content-Type', 'text/html')])
    for i in xrange(100):
        count = count + 1
        gr = gevent.spawn(api_call, i)
        gr.link_value(yielder)
    while(count > 0):
        e.wait()
        e.clear()
        item = q.get_nowait()
        yield item
    yield "Done!"
    return

def yielder(gr):
    global count, q
    count = count - 1
    q.put(gr.value)
    e.set()

def api_call(i):
    resp = urllib2.urlopen("http://graph.facebook.com/vireshas").read().strip() + " %s <br/>" % i
    return resp

server = pywsgi.WSGIServer(('', 8080), fb_call)
server.serve_forever()
