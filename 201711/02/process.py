#encoding = utf-8

""" 进程 """
import os
from multiprocessing import Process

'''
""" Linux Run Only Start """
print('Process ( %s ) start...' % os.getpid())

pid = os.fork()

if pid == 0:
	print('I am child process and my parent_process is ( %s )'
		% ( os.getpid() ))
else:
	print('I ( %s ) just created a child_process ( %s )'% ( os.getpid(), pid ))
	""" Linux Run Only End """
'''

def child_prcess_run(name):
	print('Run child process :%s ( %s )' % (name, os.getpid()))

if __name__=='__main__':
	print('Parent Process Start: ( %s )' % os.getpid())

	p = Process(target=child_prcess_run, args=('ChildProcess', ))

	print('Child process will start...')

	p.start()

	p.join()

	print('Child process end.')