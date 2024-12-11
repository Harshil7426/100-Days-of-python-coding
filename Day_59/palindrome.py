print("Palindrome checker!!!")

print("Enter a word to check if it is a palindrome")

word = input("Enter a word to check if its paliindrome: ")
def is_palindrome(word):
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  return is_palindrome(word[1:-1])
if is_palindrome(word):
  print("The word is a palindrome")
else:
  print("The word is not a palindrome")