class Triangle:
    def __init__(self, size:int, pattern:str, direction:str):
        self.size = size
        self.pattern = pattern
        self.direction = direction.upper()

    def display(self):
        if self.direction == 'L':
            for i in range(1,int(s)+1):
                print(p*i, end='')
                print()
        elif self.direction == 'R':
            for i in range(1,int(s)+1):
                for j in range(int(s)-i):
                    print(' ', end='')
                print(p*i, end='')
                print()

s = input("Enter triangle size: ")
p = input("Enter pattern: ")
d = input("Enter direction (L/R): ")

if len(p) != 1:
    print("Pattern cant exceed 1 character.")
else:
    obj = Triangle(s,p,d)
    obj.display()
