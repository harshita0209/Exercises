def is_palindrome(string) :
   if len(string) <= 1 :
      return True
   if string[0] == string[len(string) - 1] :
      return is_palindrome(string[1:len(string) - 1])
   else :
      return False

print(is_palindrome("racecar"))