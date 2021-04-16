from provided_code import d
# Code your solution here
for i in d.keys():
    if i==1 or i==2 or i==3 or i==4:
        missing=5
    elif i==1 or i==2 or i==3 or i==5:
        missing=4
    elif i==1 or i==2 or i==4 or i==5:
        missing=3
    elif i==1 or i==3 or i==4 or i==5:
        missing=2
    elif i==2 or i==3 or i==4 or i==5:
        missing=1
    else:
        missing=None
d[missing]="found it!"




