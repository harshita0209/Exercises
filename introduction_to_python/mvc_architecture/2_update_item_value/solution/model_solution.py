class Program:
    def __init__(self,program_list):
        self.program_list=program_list
    
    def get_list(self,obj1):
        # list1=[]
        # for i in obj1.keys():
        #     list1.append(i)
        # return list1
        return obj1

    def update_list_key(self,key,value,program_list):
        program_list[key]=value
        return program_list
