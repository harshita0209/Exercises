class Vector3D:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __sub__(self,other):
        str=Vector3D(self.x-other.x, self.y-other.y, self.z-other.z)
        
        return str
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec3 = Vector3D()
print(vec1 - vec2 )#== Vector3D(-3, 1, 2)
vec1 = Vector3D(1, 2, 0)
vec2 = Vector3D(y=1, z=3)
print(vec1 - vec2 )
print(vec1 - vec3 )