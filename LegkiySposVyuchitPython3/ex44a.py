class Parent(object):

    def implicit(self):
        print("Родитель implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()
dad.implicit()
son.implicit()
