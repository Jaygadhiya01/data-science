# class Hello:
#     def __init__(self):
#         print("Hello, World!")





# h1=Hello()#instance object
# h2=Hello()#instance object



# print(h1.__dict__)
# print(h2.__dict__)


class Line:
    def __init__(self,l=0):
        self.length=l



l1=Line()

print(l1.__dict__)

l2=Line(33)
print(l2.__dict__)







