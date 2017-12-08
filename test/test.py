
class Model(object):
    async def save(self):
        await 1
        pass

class User(Model):
    pass


user = User()
await user.save()