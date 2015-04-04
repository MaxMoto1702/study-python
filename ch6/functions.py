__author__ = 'm'

def func1():
    var1 = 0
    return var1
def func2():
        global var1
        var1 += 1
        return var1
var1 = 0
print("zero", func1(), var1)
print("inc", func2(), var1)
print("inc", func2(), var1)
print("zero", func1(), var1)
print("inc", func2(), var1)