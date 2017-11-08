#encoding=utf-8
from multiprocessing import Process, Queue
import time, random, os
from multiprocessing import Pool
import subprocess

""" 进程和线程 """

'''
""" 进程 """
def child_func(*args):
	print('child process( %d ) start' % ( os.getpid() ))
	time.sleep(1)
	print('I am the child process( %d ) from parent process( %d )' % ( os.getpid(), os.getppid() ))
	for arg in args:
		print(arg)

if __name__=='__main__':
	print('parent process( %d ) start' % ( os.getpid() ))
	p = Process(target=child_func, args=(1,2,3,4,5))
	p.start()
	p.join()
	print('parent process end')

def long_time_task(name):
	print('child process( %d ), parent process ( %d )' % ( os.getpid(), os.getppid() ))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
	print('parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	# p = Pool(4, long_time_task, (1,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')

print(os.getpid())
# child = subprocess.Popen(["ping","-c","5","www.google.com"])
child = subprocess.Popen("ping -c 5 www.google.com", shell=True)
child.wait()
print(child.pid)
print("parent process")
'''

""" 进程间通信 Linux only """
def write(q):
	print('Process to write: ( %d )' % ( os.getpid() ))
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read: ( %d )' % ( os.getpid() ))
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()