class my_parent:
    # magic_number = 7
    def __init__(self, number):
        self.magic_number = number;

class child1(my_parent):
    pass

# p1 = my_parent(7)
c1 = child1(7)

# print(p1.magic_number)
print(c1.magic_number)
