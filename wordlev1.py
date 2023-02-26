# this program need DL.txt file.


# read the dictionary file
def GetDic():
    try:
        dicopen = open("DL.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        return diclist
    except FileNotFoundError:
        print("No Dictionary!")
        return


# removes words containing the given letter
def grey(list1, w):
    for i in range(len(w)):
        pref1 = [x for x in list1 if w[i] not in x]
    return pref1


# removes words containing given letter in given position
def yellow(list2, y, pos):
    pref2 = [x for x in list2 if y != x[pos]]
    pref4 = [x for x in pref2 if y in x]
    return pref4


# removes words without the given letter in given position
def green(list3, z, posi):
    pref3 = [x for x in list3 if z == x[posi]]
    return pref3


# reads input containing guesses and color code of the letters.
word = input("Enter the word:")
colour = input("Grey = 1\nYellow = 2\nGreen = 3\nEnter the colour scheme:")
word = list(word)
colour = [eval(j) for j in colour]
print(word, colour)


# solves the issue of repeated letters with different colors
def skipper(letterlist, colourlist):
    d = GetDic()
    gor = [0 for x in range(5)]
    for m in range(0,5):
        for p in range(0,5):
            if colourlist[m] != 1:
                gor[m] = letterlist[m]
    print(gor)
    for i in range(0,5):
        if colourlist[i] != 1:
            # print(f'{letterlist[i]} not greys')
            if colourlist[i] == 2:
                d = yellow(d, letterlist[i], i)
            else:
                d = green(d, letterlist[i], i)
        else:
            if letterlist[i] not in gor:
                # print(f'{letterlist[i]} not repeated')
                d = grey(d, letterlist[i])
            else:
                pass
                # for k in range (0,5):
                #     if k != i:
                #         d = yellow(d, letterlist[i],k)
    return d


newlist = skipper(word, colour)
print(len(newlist))
print(newlist)
