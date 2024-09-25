def is_palindrome(num):
    return str(num) == ''.join(reversed(str(num)))
 
num = int(input("Enter number: "))
 
if is_palindrome(num):
  print(" Palindrome")
else:
  print(" Not A Palindrome")