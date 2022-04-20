def subsequences(s,o=''):
    if len(s)==0:
        print(o)
        return

    subsequences(s[1:],o)
    subsequences(s[1:],o+s[0])
    return


string = input()
subsequences(string)