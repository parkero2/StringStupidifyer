def stupidify():
    msgstr = input("Input a message here:")
    msgarr = []
    uorl = 1
    for a in range(len(msgstr)):
        msgarr.append(msgstr[a])
        if uorl == 1:
            msgarr[a] = msgarr[a].upper()
            uorl = 2
        else:
            msgarr[a] = msgarr[a].lower()
            uorl = 1
    for b in range(len(msgarr)):
        out = ''.join(msgarr)
    print(out)
    stupidify()
stupidify()