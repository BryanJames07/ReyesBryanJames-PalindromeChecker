def palchecker(s):
    s = s.lower()
    length = len(s)
    if length < 2:
        return True
    elif s[0] == s[length - 1]:
        return palchecker(s[1: length - 1])
    else:
        return False

varchar = input("Input a Word or number/s: ")
ans = palchecker(varchar)
if ans:
    print(varchar + " is a Palindrome!")
else:
    print(varchar + " is not a Palindrome!")
