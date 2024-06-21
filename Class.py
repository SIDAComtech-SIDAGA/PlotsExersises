class MyClass:
    def __init__(self,real = 0, img = 0):
        print("My Class is running")
        self.real_part = real
        self.imag_part = img
        
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.imag_part))
        
cmp1 = MyClass(19,5)
cmp1.displayComplex()
        