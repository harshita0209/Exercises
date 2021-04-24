movie_list= {1:'a',2:'b',3:'c'}
def get_list():
    return movie_list

def del_list_key(n):
    movie_list.pop(n)
    final_list=movie_list
    return final_list