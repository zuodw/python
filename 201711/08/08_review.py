#encoding=utf-8

from multiprocessing import Process, Pool
import os, time, random


def pool_func(name):
	time.sleep(0.5)
	print('child process: ( %d )' % ( os.getpid() ))

if __name__ == '__main__':
	print('parent process: ( %d )' % ( os.getpid() ))
	p = Pool(4)
	for i in range(5):
		p.apply_async(pool_func, (i,))
	p.close()
	p.join()
	print('end')