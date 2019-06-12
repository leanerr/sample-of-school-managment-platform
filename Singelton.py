class SingletonDecorator:
    def __init__(self,klass):
        self.klass = klass
        self.instance = None
    def __call__(self,*args,**kwds):
        if self.instance == None:
            self.instance = self.klass(*args,**kwds)
        return self.instance

class foo:
    def __init__(self,x=""):
        self.y=x
    def __str__(self):
        return self.y
foo = SingletonDecorator(foo)

x=foo("hi")
y=foo("hello")
z=foo("good")
t=foo()
#x.val = 'sausage'
#y.val = 'eggs'
#z.val = 'spam'
print(x)
print(y)
print(z)
print(t)
print(x is y is z is t)