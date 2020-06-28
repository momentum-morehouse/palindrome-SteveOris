import re

def is_Palindrome():
  x = input('enter phrase ')
  clean = re.sub(r'[^A-Za-z]','', x.lower())
  return clean == clean[::-1], x
   
ans = is_Palindrome()
  
if ans:
    print( ans[1], 'is a palindrome')
else: 
    print("is not a palindrome")