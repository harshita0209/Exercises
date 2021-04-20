
def reverse(string):
    newstr=""
    if len(string)==0:
        return newstr
    else:
        newstr=newstr+string[len(string)-1::-1]
        reverse(string[0:len(string)-2])
        return newstr
