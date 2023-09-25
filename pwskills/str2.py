def palindrome():
    word = str(input('enter:'))
    if word[::-1] == word:
        print(f'this is palindrome{word}')
    else:
        print(f'this is not palindrome{word}')
