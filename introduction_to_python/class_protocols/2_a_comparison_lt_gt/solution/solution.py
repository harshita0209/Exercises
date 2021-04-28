import math
class Vector3D:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __lt__(self,other):
        if math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z) < math.sqrt(other.x*other.x+other.y*other.y+other.z*other.z):
            # print(math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z))
            # print(math.sqrt(other.x*other.x+other.y*other.y+other.z*other.z))

            return True
        else:
            return False
        
    
        if math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z) > math.sqrt(other.x*other.x+other.y*other.y+other.z*other.z):
            # print(math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z))
            # print(math.sqrt(other.x*other.x+other.y*other.y+other.z*other.z))

            return True
        else:
            return False
        
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec3 = Vector3D(1, 5, 2)
print(vec1 < vec2)
print(vec1 < vec3)
print(vec1 > vec2)
print(vec1 > vec3)