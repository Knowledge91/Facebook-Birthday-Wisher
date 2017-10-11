# -*- coding: utf-8 -*-

#f = open("Birthday.ics")
#s = f.read()

toReplace = "Cumpleaños de"
#while (s.find(toReplace) != -1):
#    s = s.replace(toReplace, "", s.find(toReplace)-1)

sOut = ""
with open("Birthday.ics") as f:
    for line in f:
        if (line.find(toReplace) != -1):
            # delete toReplace
            line1 = line.replace(toReplace, "")
            sOut = sOut + line1
            # look for empty space after SUMMARY:
            # sOut = sOut + line1[0:line1.find(" ", 10)] + "\n"
        else:
            sOut = sOut + line

fOut = open("BirthdayPrepared.ics", "w")
fOut.write(sOut)
fOut.close()
