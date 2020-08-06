def no_dups(s):
    uniqs = ''
    setty = set()
    for x in s.split(" "):
        if not(x in uniqs):
            if len(uniqs) > 0:
                x = " " + x    
            uniqs = uniqs + x
             
    return uniqs


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))