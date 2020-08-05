from string import punctuation
def word_count(s):
    d = {}
    p = ["\"", ':', ";", ",", ".", '-', "+", '=', '/', '\\', "|", "[", "]", '{', '}', '(', ')', '*', '^', '&', '\'\'']
    words = s.split()

    for w in words:
        w = w.lower()
        w = ''.join(c for c in w if c not in p)
        if w in d:
            d[w] += 1
        else:
            if w:
                d[w] = 1
    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))