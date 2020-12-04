class Parent(object):

    def altered(self):
        print("Родитель altered()")
class Child(Parent):

    def altered(self):
        print(" Потомок, до вызова altered() в Родителе")
        super(Child,self).altered()
        print(" Потомок после вызова altered() в Родителе")


dad = Parent()
son = Child()

dad.altered()
son.altered()