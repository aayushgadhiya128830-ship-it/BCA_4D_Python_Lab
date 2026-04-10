class Demo:
    def add(self, a=None, b=None, c=None):
        if a and b and c:
            return a + b + c
        elif a and b:
            return a + b
        else:
            return a

d = Demo()
print(d.add(2))
print(d.add(2,3))
print(d.add(2,3,4))
