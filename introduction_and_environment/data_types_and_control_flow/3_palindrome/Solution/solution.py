# Code your solution here
word=str(input("Enter any string: "))
str=word[-1::-1]
if word == str:
    is_palindrome= True
else:
    is_palindrome= False
