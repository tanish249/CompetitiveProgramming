def isAnagram(s, t):
    h=sorted(list(s))
    g=sorted(list(t))
    if h==g:
        return "YES"
    else:
        return "NO"