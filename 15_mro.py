class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):
    pass

# Create an object of D and call show()
d = D()
d.show()

# Print the MRO
print("Method Resolution Order (MRO):")
print(D.__mro__)
