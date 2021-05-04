class Vector3D:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        
        str=Vector3D(self.x+other.x, self.y+other.y, self.z+other.z)
        
        return str
vec1 = Vector3D(1, 2, 3)
vec2 = Vector3D(4, 5, 6)
print(vec1 + vec2) #= Vector3D(5, 7, 9)
