def palindrome_sentence(word):
    string = ""


    for m in word:
        string += m

        return m[::-1] == string

    
    sentence = input('write your sentence : ')

if palindrome_sentence(sentence):
    print("'{}' is a palindrome_sentence".format(sentence))

else:
    print("'{}' is not palindrome_sentence".format(sentence))