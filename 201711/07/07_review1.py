#encoding=utf-8
import logging
logging.basicConfig(level=logging.INFO)

""" 错误、调试和测试 """

""" 错误处理 """
class MyError(ZeroDivisionError):
    pass

def func(num):
    try:
        # if num == 0:
        #     raise MyError
        result = 10 / num
        print('result is ', result)
    except ZeroDivisionError as e:
        # logging.exception(e)
        print(e)
    except MyError as me:
        # logging.exception('MyError: ', me)
        print('MyError: ', me)
    finally:
        print('finally...')

func(0)

""" 调试 """

def fun1(num):
    assert num != 0, 'num is 0'

fun1(1)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)