def is_palindrome(string):
    return string[::-1] == string



word = input("Enter your word : ")

if is_palindrome(word):
    print("'{}' is a palindrome".format(word))

else:
    print("'{}' is not a palindrome".format(word))





