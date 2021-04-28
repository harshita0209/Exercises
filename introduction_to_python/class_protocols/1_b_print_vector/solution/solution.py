class Vector3D:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        # super().__init__(x,y,z)
        str=(f'(x = {self.x}, y = {self.y}, z = {self.z})')
        return str
# a=Vector3D(10,z=3)
# print(a)
print(Vector3D(3, 4, 2))