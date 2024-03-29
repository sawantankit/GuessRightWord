import string

w = 'happiness'
count = ['*'] * 9


def hangman(c, count):
    if len(c) == 1:
        for i in range(len(w)):
            if c == w[i]:
                count[i] = c

        return count
    else:
        if w == c:
            return True
        else:
            return False


while True:
    c = input("Enter either one letter or the entire word: ")
    if len(c) == 1:
        count = hangman(c, count)
        print(*count)
        # https://www.quora.com/In-Python-how-do-you-convert-a-list-to-a-string
        if w == (''.join(count)):
            print("Well you guessed it right!")
            break

    elif len(c) == len(w):
        t = hangman(c, count)
        if t == True:
            print(c)
            break
        else:
            print("Sorry the input is wrong")
    else:
        print("Pls enter one letter or the entire word")