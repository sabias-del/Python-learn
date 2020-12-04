

class Parent(object):

    def override(self):
        print(" Родитель override()")

    def implicit(self):
        print(" Родитель implicit()")

    def altered(self):
        print(" Родитель altered()")

class Child(Parent):
    def override(self):
        print(" Потомок override()")

    def altered(self):
        print(" Потомок, до вызова altered() в Родителе")
        super(Child, self).altered()
        print(" Потомок, после вызова altered() в Родителе")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
