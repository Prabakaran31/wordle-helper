def GetDic():
    try:
        dicopen = open("DL.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        # diclist = RemoveFromList(diclist, '')
        return diclist
    except FileNotFoundError:
        print("No Dictionary!")
        return


def grey(list1, w):
    print(f'w is {w}')
    for i in range(len(w)):
        pref1 = [x for x in list1 if w[i] not in x]
    return pref1


def yellow(list2, y, pos):
    pref2 = [x for x in list2 if y != x[pos]]
    pref4 = [x for x in pref2 if y in x]
    return pref4


def green(list3, z, posi):
    pref3 = [x for x in list3 if z == x[posi]]
    return pref3


# d = GetDic()

word = input("Enter the word:")
colour = input("Grey = 1\nYellow = 2\nGreen = 3\nEnter the colour scheme:")
word = list(word)
colour = [eval(j) for j in colour]
print(word, colour)
# for i in range(0,5):
#     if colour[i] == 1:
#         d = grey(d, word[i])
#     elif colour[i] == 2:
#         d = yellow(d, word[i], i)
#     elif colour[i] == 3:
#         d = green(d, word[i], i)
#     else:
#         print("Error in input")
#
# print(len(d))
# print(d)


def skippy(letterlist, colourlist):
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


dicky = skippy(word, colour)
print(len(dicky))
print(dicky)
