#encoding=utf-8

import time, threading

""" 多线程 """
def loop(name):
	print('thread(%s) is running.' % (threading.current_thread().name))
	time.sleep(0.5)
	print('thread(%s) is end.' % (threading.current_thread().name))
	
print('thread(%s) is running.' % (threading.current_thread().name))
t = threading.Thread(target=loop, args=('zz',), name='LoopThread')
t.start()
t.join()
print('thread(%s) is end.' % (threading.current_thread().name))


value = 0
lock = threading.Lock()

def change_value(num):
	global value
	value = value + num
	value = value - num
def thread_func(num):
	for i in range(1000000):
		# lock.acquire()
		# try:
		# 	change_value(num)
		# finally:
		# 	lock.release()
		with lock:
			change_value(num)
t1 = threading.Thread(target=thread_func, args=(5,))
t2 = threading.Thread(target=thread_func, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(value)

""" ThreadLocal """
local_student = threading.local()

def local_student():
	print('student(%s) in (%s)' % (local_student.name, threading.current_thread().name))

def local_process(name):
	local_student.name = name
	local_student()

t1 = threading.Thread(target=local_process, args=('Peter',), name='Thread_A')
t2 = threading.Thread(target=local_process, args=('Sylar',), name='Thread_B')
t1.start()
t2.start()
t1.join()
t2.join()