class Vector3D:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __eq__(self,other):
        # super().__init__(x,y,z)
        if self.x==other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
        
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec3 = Vector3D(1, 5, 3)

print(vec1 == vec2)
print(vec1 == vec3)
 
