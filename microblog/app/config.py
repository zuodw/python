# only uppercase keys are added to the config.

# CSRF_ENABLED 配置是为了激活跨站点请求伪造保护。
# 在大多数情况下，你需要激活该配置使得你的应用程序更安全些。
CSRF_ENABLED = True

# SECRET_KEY设置当CSRF启用时有效，
# 这将生成一个加密的token供表单验证使用，
# 你要确保这个KEY足够复杂不会被简单推测。
SECRET_KEY = 'you-will-never-guess'