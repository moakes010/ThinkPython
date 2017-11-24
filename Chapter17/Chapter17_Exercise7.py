

class Kangaroo(object):

    def __init__(self, content=[]):
        
        _init = False
        if _init == False:
            content = []
            _init = True
        self.pouch_contents = content

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        ret=[]
        for obj in self.pouch_contents:
            ret.append(object.__str__(obj))
        return str(ret)


kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch("cellphone")
kanga.put_in_pouch("keys")
kanga.put_in_pouch("wallet")
roo.put_in_pouch("stuff")
kanga.put_in_pouch(roo)
print(kanga)
print(roo)



