class ChildClass: 
    def __init__(self):
        from importlib import import_module
        instance=import_module('parent')
        self.myClass=instance.ParentClass()

    def methodX(self):
        self.myClass.parentMethod()

    def anAbstractMethod(myClass):
        print("re-implemented by child!")

    def methodY(self):
        self.myClass.anAbstractMethod()
        self.myClass.anAbstractMethod = self.anAbstractMethod 
        self.myClass.anAbstractMethod() 
        print('I am method Y in child class!')



instance = ChildClass()
instance.methodX()
instance.methodY()