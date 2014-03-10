from gevent import pywsgi
import time
import urllib2

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return fb_call()

def fb_call():
    for i in xrange(10):
        yield urllib2.urlopen("https://graph.facebook.com/vireshas").read().strip() + " %s <br/>" % i

server = pywsgi.WSGIServer(('', 8080), hello_world)

server.serve_forever()
