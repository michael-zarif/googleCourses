class A:
    pubA = "Public A"
    _protA = "Protected A"
    __privA = "Private A"
    def show(self):
        print(self.pubA)
        print(self._protA)
        print(self.__privA)

class B(A):
    pubB = "Public B"
    _protB = "Protected B"
    __privB = "Private B"

    # Private attributes can be accessed/modified/deleted through class methods (account_index.e. getter, setter, deleter)
    @property   # Getter (can be also @privB.getter)
    def privB(self):
        return self.__privB
    @privB.setter
    def privB(self, value):
        self.__privB = value
    @privB.deleter
    def privB(self):
        del self.__privB
    def showA(self):
        print(self.pubA)
        print(self._protA)
        print(self.__privA)

a = A()
a.show()    # Private attributes can be accessed/modified/deleted through class methods (account_index.e. getter, setter, deleter)
print(a.pubA)
print(a._protA)
# print(a.__privA)    # Error: 'A' object has no attribute '__privA' (Private attribute can't be accessed using dot notation)
print(a._A__privA)    # Name Mangling can be used to access Private attributes, however, it's not recommended

b = B()
b.show()    # Doesn't give an error for private attributes, as it calls the show function from A class itself
# b.showA()    # Error: 'B' object has no attribute '_B__privA' (Private attribute can't be inherited to a derived class)
b.privB = "Private B Modified"  # Private attribute modified using property setter
print(b.privB)  # Private attribute using setter
del b.privB  # Private attribute deleted using deleter
print(b.privB)  # Prints the old value of privB in b instance before modification
