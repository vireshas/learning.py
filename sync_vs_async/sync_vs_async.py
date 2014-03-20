import gevent
import random
import time

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def task(pid):
    """
    Some non-deterministic task
    """
    secs = random.randint(0, 10)
    gevent.sleep(secs)
    print('Task %s done in [ %s ] seconds' % (pid, secs))

def synchronous():
    print('Started synchronous: %s' % tic())
    for i in range(1,10): #runs one by one, gevent sleeps when the task runs
        task(i)
    print('Ended synchronous: %s' % tic())

def asynchronous():
    print('Started asynchronous: %s' % tic())
    threads = [gevent.spawn(task, i) for i in xrange(10)] #runs "at the same time", gevent sleeps "at the same time"
    gevent.joinall(threads)
    print('Ended asynchronous: %s' % tic())

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
