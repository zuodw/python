#encoding=utf-8
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(username, passwd):
	real_passwd = db[username]
	md5 = hashlib.md5()
	md5.update(passwd.encode('utf-8'))
	input_passwd = md5.hexdigest()
	print(real_passwd, input_passwd)
	if real_passwd == input_passwd:
		return True
	else:
		return False

print(login('michael', '123456'))
print(login('bob', 'asfasfasdf'))
