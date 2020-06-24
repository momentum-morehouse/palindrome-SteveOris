

def isPalindrome():
  x = input('enter phrase')
  return x == x[::-1] 
ans = isPalindrome()
  
if ans:
    print("Yes") 
else: 
    print("No") 