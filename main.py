

def isPalindrome():
  x = input('enter phrase')
  return x == x[::-1]
   
ans = isPalindrome()
  
if ans:
    print("is a palindrome") 
else: 
    print("is not a palindrome")